# Salarium 

Script to automate time-in and time-out on Salarium.

## Usage

1. Configure hosts file with ip address, set user and group for file permissions and configure target host timezone. 
2. To install script on host, use salarium role.

```
ansible-playbook -i ansible/hosts ansible/main.yml --tags=salarium
```

3. Enable Salarium crontab using salarium-enable role.

```
ansible-playbook -i ansible/hosts ansible/main.yml --tags=salarium-enable
```

4. Holidays are handled using python-holidays library. You can set your country and region as you desire. 

5. On unscheduled dates (e.g. sick leave) where you don't need to time in/out you need to manually disable the crontab using salarium-disable role. Take note you'll need to run salarium-enable role again, preferably before the next time in.

6. You can also reconfigure time in/out randomness by adjusting crontab sleep delay on salarium-enable/disable roles. Script currently has a delay of 0 to 120 seconds. Adjust accordingly.

```
ansible-playbook -i ansible/hosts ansible/main.yml --tags=salarium-disable
```

## Acknowledgements

[Jerico Aragon](https://github.com/jerico)'s [curl script](https://gist.github.com/jerico/a9e0272176028f53d9615f3bb745a134)