# xmr-stak

This bundle will build and configure [xmr-stak](https://github.com/fireice-uk/xmr-stak) to mine monero or aeon.
In the current version only CPU mining is supported by the bundle.
Additional setup steps are required.

## Requirements

* Bundles:
  * [dnf](https://github.com/rullmann/bundlewrap-dnf)
  * [python](https://github.com/rullmann/bundlewrap-python)

## Setup notes

As xmr-stak config files are especially written for a specific machine they're not being configured with metadata.
Instead the config needs to be generated prior to usage. To do so a `bootstrap` mode has been implemented.

First assign this bundle to a node and add the following metadata:

    'metadata': {
        'xmr-stak': {
            'bootstrap': True,
        },
    }

Now apply the changes to your node.
On your node switch to user 'xmrstak' and run the initial setup:

    # su - xmrstak
    $ cd /opt/xmr-stak-bin/bin/
    $ ./xmr-stak

This will prompt you to enter the required information to create a config file.
After this steps have been performed you can find two files beside the `xmr-stak` binary: `config.txt`, `cpu.txt`

Copy these to your machine and put them in the xmr-stak-bundle data directory: `data/xmr-stak/files`
Please consider the required naming scheme: `<node.name>.config.txt`, `<node.name>.cpu.txt`

Now you can safely remove the `bootstrap` option and apply again. By doing so the xmr-stak service will be enabled. 

## Integrations

* Bundles:
  * [telegraf](https://github.com/rullmann/bundlewrap-telegraf)

## Metadata

    'metadata': {
        'xmr-stak': {
            'bootstrap': False, # optional, required for initial setup only
        },
    }
