@metadata_processor
def dnf(metadata):
    if node.has_bundle('dnf'):
        metadata.setdefault('dnf', {})
        metadata['dnf'].setdefault('extra_packages', [])
        for package in ['cmake', 'libmicrohttpd-devel', 'openssl-devel', 'hwloc-devel']:
            if package not in metadata['dnf']['extra_packages']:
                metadata['dnf']['extra_packages'].append(package)
    return metadata, DONE

@metadata_processor
def pip(metadata):
    if node.has_bundle('python') and node.has_bundle('telegraf'):
        metadata.setdefault('python', {})
        metadata['python'].setdefault('pip_packages', [])
        for package in ['requests']:
            if package not in metadata['python']['pip_packages']:
                metadata['python']['pip_packages'].append(package)
    return metadata, DONE
