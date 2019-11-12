# NoDistractions_WebsiteBlocker
This application blocks distracting websites of your choice! First,(if you are using windows), change the host file location to the following, C:\Windows\System32\drivers\etc. Next, inside the website list variable, insert the websites you want to block during the set time. Finally, change the script to incorporate your new python application. 

For mac, type the following in the terminal sudo crontab -e. Inside the text editor write, @reboot python_script_path. Restart your computer and your application should start working!

For Windows, create a duplicate of the OS host file and provide the path of the duplicate in the host path used in the script. Create a task and create a task name (make sure you write it with the highest privleges). At triggers, select "At Startup". Then, at the action bar, create a new action and put in your path to the script. At the conditions bar, unflag the power section, press Ok and the script will be scheduled. Restart your computer and your application should start working!
