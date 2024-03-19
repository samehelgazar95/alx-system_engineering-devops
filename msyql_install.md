[How to : ] Fresh Reset and Install mysql 5.7
 ⚠️ Before going through the guide try this command if it gonna install MySQL 5.7 correctly, when you see the white windows you can jump to step 9, and see what to choose :

 sudo wget -O mysql57 https://raw.githubusercontent.com/nuuxcode/alx-system_engineering-devops/master/scripts/mysql57 && sudo chmod +x mysql57 &&  sudo ./mysql57
If this command did not install 5.7 correctly you can continue reading the following guide.

NOTE AS YOU PROCEED: At any point in this guide, don’t go to the next step if you have errors in the current step you are in, make sure there are no errors.

You can also use this guide for more visual and sample outputs :

For a comprehensive Guide Click Here 📄
STEPS :
Clean Running MySQL Processes :

Check for any running MYSQL Processes: sudo ps aux | grep mysql
If MySQL is running,try stopping it : sudo service mysql stop
Double-check if MySQL is no longer running: sudo ps aux | grep mysql
If MySQL processes are still running, terminate them, remember to replace PID with the value of your PID : sudo kill -9 <PID>
Remove Existing MySQL Versions:

Remove MySQL packages sudo apt-get remove --purge mysql-server mysql-client mysql-common -y && sudo apt-get autoremove -y
If no errors occurs, proceed to next steps
If prompted by a dialog to remove data directories, please select YES and press Enter.
Remove MySQL Apt Configurations :

Running the following :::
sudo rm -rf /etc/apt/sources.list.d/mysql.list*
sudo rm -rf /var/lib/mysql-apt-config
sudo dpkg --purge mysql-apt-config
Double Check and Remove Configuration File

Check by running : dpkg -l | grep mysql
The result from above should be none, on your terminal
Now, Remove configurations files by : sudo rm -rf /etc/mysql /var/lib/mysql
Edit sources.list to Remove MySQL Repositories :

Check the sources.list file for MySQL repository entries (example: deb http://repo.mysql.com/apt/ubuntu bionic main), there should be none like the picture below:
Update the packages :

Check the sources.list file for MySQL repository entries (example: deb http://repo.mysql.com/apt/ubuntu bionic main),
Run : cat /etc/apt/sources.list | grep mysql
there should be none like the picture below:
If there are entries, open the sources.list file: sudo vi /etc/apt/sources.list
If no errors occur, proceed to the next step.
Update the package by running :** sudo apt update**
Kill any running processses ps aux | grep apt
Clean APT Cache :

Run : sudo apt clean
Configure any Pending Packages and Install MySQL :

Run :
sudo dpkg --configure -a
Install MySQL by running : ** sudo wget -O mysql57 https://raw.githubusercontent.com/nuuxcode/alx-system_engineering-devops/master/scripts/mysql57 && sudo chmod +x mysql57 && sudo ./mysql57**
A few windows are going to show up, Follow the prompts to select Ubuntu Bionic, change to MySQL 5.7 and set a password if needed.
After installation, check MySQL status: sudo service mysql status *
If issues persist, use the following commands to debug :
journalctl -u mysql.service
cat /var/log/mysql/error.log
journalctl -xe
Check this post o learn more about MySQL
https://shazaali.substack.com/p/database-administration
