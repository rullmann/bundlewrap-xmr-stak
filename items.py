svc_systemd = {}

files = {
    '/etc/systemd/system/xmr-stak.service': {
        'content_type': 'mako',
        'mode': '0644',
        'source': 'xmr-stak.service',
        'triggers': ['action:systemd-daemon-reload'],
    },
    '/etc/security/limits.d/01-xmrstak.conf': {
        'mode': '0444',
        'source': 'limits.conf',
    },
}

users = {
    'xmrstak': {
        'gid': 1100,
        'home': '/opt/xmr-stak-bin',
        'shell': '/bin/bash',
        'uid': 1100,
    },
}

groups = {
    'xmrstak': {
        'gid': 1100,
    },
}

directories = {
    '/opt/xmr-stak': {
        'mode': '0755',
        'owner': 'xmrstak',
        'group': 'xmrstak',
    },
    '/opt/xmr-stak-bin': {
        'mode': '6755',
        'owner': 'xmrstak',
        'group': 'xmrstak',
    },
    '/opt/xmr-stak-bin/bin': {
        'mode': '6755',
        'owner': 'xmrstak',
        'group': 'xmrstak',
    },
}

git_deploy = {
    '/opt/xmr-stak': {
        'needs': ['directory:/opt/xmr-stak', 'directory:/opt/xmr-stak-bin'],
        'repo': 'https://github.com/fireice-uk/xmr-stak.git',
        'rev': 'master',
        'triggers': ['action:xmr-stak_cmake'],
    },
}

actions = {
    'xmr-stak_cmake': {
        'command': 'cd /opt/xmr-stak && cmake . -DCUDA_ENABLE=OFF -DOpenCL_ENABLE=OFF -DCPU_ENABLE=ON -DCMAKE_INSTALL_PREFIX=/opt/xmr-stak-bin && make install',
        'triggered': True,
        'triggers': ['svc_systemd:xmr-stak:restart'],
    },
}

if not node.metadata.get('xmr-stak', {}).get('bootstrap', False):
    files['/opt/xmr-stak-bin/bin/config.txt'] = {
        'mode': '0664',
        'source': '{}.config.txt'.format(node.name),
        'owner': 'xmrstak',
        'group': 'xmrstak',
        'triggers': ['svc_systemd:xmr-stak:restart'],
    }

    files['/opt/xmr-stak-bin/bin/cpu.txt'] = {
        'mode': '0664',
        'source': '{}.cpu.txt'.format(node.name),
        'owner': 'xmrstak',
        'group': 'xmrstak',
        'triggers': ['svc_systemd:xmr-stak:restart'],
    }

    files['/opt/xmr-stak-bin/bin/pools.txt'] = {
        'mode': '0664',
        'source': '{}.pools.txt'.format(node.name),
        'owner': 'xmrstak',
        'group': 'xmrstak',
        'triggers': ['svc_systemd:xmr-stak:restart'],
    }

    svc_systemd['xmr-stak'] = {
        'needs': ['file:/etc/systemd/system/xmr-stak.service'],
    }
