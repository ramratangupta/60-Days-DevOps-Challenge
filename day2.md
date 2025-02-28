* **Challenge 1:** Write a simple Bash script that prints “Hello DevOps” along with the current date and time.
```
#!/bin/bash
echo "Hello DevOps , `date +"%Y-%m-%d %H:%M:%S"`"
```
* **Challenge 2:** Create a script that checks if a website (e.g., https://www.learnxops.com) is reachable using curl or ping. Print a success or failure message.

```
#!/bin/bash
URL=https://www.learnxops.com
CHECK=`curl -Is $URL`
if [[ -z $CHECK ]]; then
    echo "${URL} Not Reachable"
else
    echo "${URL} Reachable"
fi
```
* **Challenge 3:** Write a script that takes a filename as an argument, checks if it exists, and prints the content of the file accordingly.

```
#!/bin/bash
FILENAME=$1
if [[ -z $FILENAME ]];then
    echo "File name is empty"
    exit 1
fi

if [[ -f $FILENAE ]];then
    cat $FILENAME
    exit 0
else:
    echo "File not exits"
    exit 1
fi

```

* **Challenge 4:** Create a script that lists all running processes and writes the output to a file named process_list.txt.

```
#!/bin/bash
ps -ef >process_list.txt
```
* **Challenge 5:** Write a script that installs multiple packages at once (e.g., git, vim, curl). The script should check if each package is already installed before attempting installation.
```
#!/bin/bash
PACKAGES="git vim curl"
for PACKAGE in $PACKAGES;do
    echo "Checking $PACKAGE"
    if [[ -z `which $PACKAGE` ]];then
        sudo apt install $PACKAGE -f
    else
        echo "$PACKAGE is already installed"
    fi
done
```
* **Challenge 6:** Create a script that monitors CPU and memory usage every 5 seconds and logs the results to a file.
```
#!/bin/bash
LOGFILENAME="ram_cpu_usages.txt"
echo -e "Timestamp\t\tRAM Used\tCPU Used" > $LOGFILENAME
while true;do
    USEDMEMORY=`free -h | grep Mem | awk '{print $3}'`
    USEDCPU=`top -bn1 | grep "Cpu(s)" | awk '{print $2}'`
    TIMESTAMP=`date +"%Y-%m-%d %H:%m:%S"`
    echo -e "${TIMESTAMP}\t${USEDMEMORY}\t\t${USEDCPU}" >> $LOGFILENAME
    sleep 5
done

```
-e enables interpretation of backslash escapes

\t adds tab spacing for formatting

\> overwrites or create file (first time setup)
\>> Keep appending the file
top -bn1 runs top command in batch mode (-b) for 1 iteration (-n1)

free -h shows memory usage in human-readable format

* **Challenge 7:** Write a script that automatically deletes log files older than 7 days from /var/log.
```
LISTFILES=`find /var/log -type f -mtime +7`
if [[ $EUID -ne 0 ]]; then
    echo "Run as root"
    exit 1
fi
for file in $LISTFILES; do
    rm $file
done
```
* **Challenge 8:** Automate user account creation – Write a script that takes the username as an argument, checks, if the user exists, gives the message “user already exists“ else creates a new user, adds it to a “devops“ group, and sets up a default home directory.
```
#!/bin/bash
if [[ `id -u` -ne 0 ]];then
    echo "Run this as root"
    exit 1
fi
if [[ -z $1 ]];then
    echo "User name can not be empty"
    echo "Usage: $0 <username>"
    exit 1
fi
USERNAME=$1
if [[ -z `id -u $USERNAME` ]];then
    useradd -m -G devops $USERNAME
else
    echo "$USERNAME user exits"
fi
```
* **Challenge 9:** Use awk or sed in a script to process a log file and extract only error messages.
```
LOGFILE=/var/log/nginx/error.log
cat $LOGFILE | grep error
```
* **Challenge 10:** Set up a cron job that runs a script to back up (zip/tar) a directory daily.
```
FOLDER=~/Pictures

DATE=`date +"%Y_%m_%d_%H_%M_%S"`
FILENAME="Pictures_${DATE}.zip"
cd $FOLDER
zip -r $FILENAME .
#Move to backuppath or in S3
mv $FILENAME ../
```

Save above in backup_pictures.sh
chmod 777 backup_pictures.sh
```
#Every day 12 AM
0 0 * * * backup_pictures.sh
```
* **💡 Bonus Challenge:** Customize your Bash prompt to display the current user and working directory. (Hint:** export PS1="\u@\h:\w\$ "), try to make it permanent, so terminal closing and opening don’t default!

```
echo "export PS1=\"\u@\h:\w\$ \"" >> ~/.bashrc
source ~/.bashrc
```
