# installation instructions
Because this plugin isn't part of a collection it needs to be installed manually.  
There are few possible ways and locations it can be installed.

By using [BECOME_PLUGIN_PATH](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#become-plugin-path) or `ANSIBLE_BECOME_PLUGIS` environment variable.

## As a single file
```
cd ~/.ansible/plugins/become
wget https://raw.githubusercontent.com/chramb/ansible.become.podman_unshare/master/plugins/become/podman_unshare.py
```

## Locally for selected playbooks or single role
This way only selected roles or playbooks will have access to this plugin.
for whole playbook and single role respectively.

**for whole playbook**
`<playbook>/become_plugins/`

**for single role**
`<playbook>/roles/<role>/become_plugins/`

## As a repository
Clone it anywhere in your filesystem, for example `~/.ansible/plugins/become/`.
```shell
git clone --depth 1 https://github.com/chramb/ansible.become.podman_unshare/edit/master/README.md \
     $HOME/.ansible/plugins/become/podman_unshare/
```
then configure ansible.cfg to source plugin from chosen path by adding it to correct path.
```ini
# ansible.cfg
[defaults]
become_plugins = "~/.ansible/plugins/become:/usr/share/ansible/plugins/become:~/.ansible/plugins/become/podman_unshare/plugins/become/:/usr/share/ansible/plugins/become/podman_unshare
```
This can be also done for a single playbook.

---
more information in the [official documentation](https://docs.ansible.com/ansible/latest/dev_guide/developing_locally.html)
