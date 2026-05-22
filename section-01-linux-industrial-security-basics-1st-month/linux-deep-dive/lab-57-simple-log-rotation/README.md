# Lab 57: Simple Log Rotation

## Objectives

- Understand the basics of log rotation in Linux.
- Learn how to inspect and modify logrotate configuration files.
- Manually trigger log rotation.
- Verify rotated and compressed log files.

---

# Prerequisites

- Linux system with sudo privileges
- Basic Linux command knowledge
- Familiarity with system logs

---

# Task 1 — Check Default Configuration in `/etc/logrotate.conf`

## View Default Configuration

```bash
cat /etc/logrotate.conf
```

## Example Output

```conf
weekly
rotate 4
create
compress
```

## Explanation

| Setting | Description |
|---|---|
| weekly | Rotate logs weekly |
| rotate 4 | Keep 4 old log files |
| create | Create new log files after rotation |
| compress | Compress old rotated logs |

---

# Task 2 — Inspect a File in `/etc/logrotate.d/`

## Navigate to Configuration Directory

```bash
cd /etc/logrotate.d
```

## List Available Configurations

```bash
ls
```

## Open a Configuration File

Example:

```bash
cat apache2
```

## Example Configuration

```conf
/var/log/apache2/*.log {
    weekly
    missingok
    rotate 14
    compress
    delaycompress
    notifempty
    create 640 root adm
    sharedscripts
    postrotate
        if [ -f /var/run/apache2.pid ]; then
            /etc/init.d/apache2 reload > /dev/null
        fi
    endscript
}
```

## Important Settings

| Setting | Description |
|---|---|
| missingok | Ignore missing log files |
| notifempty | Do not rotate empty logs |
| delaycompress | Compress logs on next rotation cycle |
| postrotate | Execute commands after rotation |
| create 640 | Create new logs with permissions |

---

# Task 3 — Manually Force Log Rotation

## Force Log Rotation

```bash
sudo logrotate --force /etc/logrotate.conf
```

## Verify Rotation

```bash
ls -ltr /var/log
```

## Check Compressed Logs

```bash
ls /var/log/*.gz
```

---

# Verification

- Logs rotated successfully
- Old logs compressed using `.gz`
- New log files created automatically
- Rotation rules followed according to configuration

---

# Conclusion

In this lab, we learned how log rotation works in Linux systems using `logrotate`.

We inspected:
- Global configuration in `/etc/logrotate.conf`
- Service-specific configurations in `/etc/logrotate.d/`

We also manually triggered log rotation and verified rotated/compressed log files.

This process helps manage disk usage and keeps system logs organized efficiently.
