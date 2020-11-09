import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import subprocess as sp
import smtplib
import getpass

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# change voice (voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hii, How may I help you")     
  

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)


    try:
        print("Recognizing...")    
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def sendEmail(whom, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('18erecs013.ashish@rietjaipur.ac.in', 'Ashrad99!')
    server.sendmail('18erecs013.ashish@rietjaipur.ac.in', whom, content)
    server.close()

def remove(string): 
    return string.replace(" ", "")

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            print("opening youtube")
            speak("opening youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            print("opening google")
            speak("opening google")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com") 
            print("opening stack overflow")
            speak("opening stack overflow")  


        elif 'play tv series' in query:
            music_dir = 'F:/entertainment/tv series/12 Monkeys/s1'# put you music dir here
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            print("opening youtube")
            speak("opening youtube")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"the time is {strTime}")
            speak(f"the time is {strTime}")



        elif 'run command' in query:
            speak("what you want to run")
            app = remove(takeCommand())
            x = sp.getoutput("start"+" "+"/MIN"+" "+app)

        elif 'run docker' in query:
            webbrowser.open("commands.html")



##############################################  Hadoop Script start ##################################################################################       

        elif 'setup hadoop' in query:
            speak("your master node ip")
            masterIp = input("Enter your Aws instance IP : ").replace(".", "-")
            passMaster = input("pem file name : ")
            speak("1 to setup namenode  or 2 to run name node")
            value = int(input('''1 to setup namenode:\n 2 to run name node: '''))
            if value == 2:
                os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo hadoop-daemon.sh start namenode'.format(passMaster, masterIp))
            elif value == 1:     
                os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo yum install wget -y'.format(passMaster, masterIp))
                os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo wget -O /home/hadoop-1.2.1-1.x86_64.rpm https://jokker99.s3.ap-south-1.amazonaws.com/hadoop-1.2.1-1.x86_64.rpm'.format(passMaster, masterIp))
                os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo wget -O /home/jdk-8u171-linux-x64.rpm https://jokker99.s3.ap-south-1.amazonaws.com/softwares/jdk-8u171-linux-x64.rpm'.format(passMaster, masterIp))
                print(os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo rpm -ivh /home/jdk-8u171-linux-x64.rpm'.format(passMaster, masterIp)))
                print(os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo rpm -ivh /home/hadoop-1.2.1-1.x86_64.rpm --force'.format(passMaster, masterIp)))
                os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo wget -O /etc/hadoop/core-site.xml https://jokker99.s3.ap-south-1.amazonaws.com/master+node/core-site.xml'.format(passMaster, masterIp))
                os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo wget -O /etc/hadoop/hdfs-site.xml https://jokker99.s3.ap-south-1.amazonaws.com/master+node/hdfs-site.xml?versionId=OJ19K5SOxNfzBg34ykHCPJdNqsIZ2XdR'.format(passMaster, masterIp))
                os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo mkdir /master'.format(passMaster, masterIp))
                os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo hadoop namenode -format -force'.format(passMaster, masterIp))
                os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo hadoop-daemon.sh start namenode'.format(passMaster, masterIp))
            else:
                speak("option not aviliable")
                print("option not aviliable")


            with open('core-site.xml') as f:
                rewrite=f.read().replace('0.0.0.0', masterIp.replace("-","."))
            with open('core-site.xml', "w") as f:
                f.write(rewrite)
            os.system('aws s3 cp core-site.xml s3://jokker99/core-site/ --acl public-read')


            
##---------------------------------------------------------------------------------------------------------------------------------------------##               
            speak("How many nodes do you have")
            listOfNodes = []
            nodepass = input("pem file name : ")
            no_of_node = int(input("How many nodes do you have: "))

            for i in range(no_of_node):
                nodeIp = input("Enter your Aws instance IP : ").replace(".", "-")
                listOfNodes.append(nodeIp)
            
            speak('''1 With L VM
            2 Without L V M ''')
            lvmset = int(input('''1. With L VM
            2. Without L V M '''))

            for i in range(0,no_of_node):
                os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo yum install wget -y'.format(nodepass, listOfNodes[i]))
                os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo wget -O /home/hadoop-1.2.1-1.x86_64.rpm https://jokker99.s3.ap-south-1.amazonaws.com/hadoop-1.2.1-1.x86_64.rpm'.format(nodepass, listOfNodes[i]))
                os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo wget -O /home/jdk-8u171-linux-x64.rpm https://jokker99.s3.ap-south-1.amazonaws.com/softwares/jdk-8u171-linux-x64.rpm'.format(nodepass, listOfNodes[i]))
                print(os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo rpm -ivh /home/jdk-8u171-linux-x64.rpm'.format(nodepass, listOfNodes[i])))
                print(os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo rpm -ivh /home/hadoop-1.2.1-1.x86_64.rpm --force'.format(nodepass, listOfNodes[i])))
                os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo wget -O /etc/hadoop/core-site.xml https://jokker99.s3.ap-south-1.amazonaws.com/core-site/core-site.xml'.format(nodepass, listOfNodes[i]))  
                 
                if lvmset == 1 :
                    speak("feature comming soon")
                    print("feature comming soon")
                if lvmset == 2 :
                    os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo wget -O /etc/hadoop/hdfs-site.xml https://jokker99.s3.ap-south-1.amazonaws.com/datanode/hdfs-site.xml'.format(nodepass, listOfNodes[i]))



##---------------------------------------------------------------------------------------------------------------------------------------------## 
            speak("How many clients do you have")
            listOfClients = []
            no_of_clients = int(input("How many clients do you have: "))
            clientspass = input("pem file name : ")
            for j in range(no_of_clients):
                ClientIp = input("Enter your Aws instance IP : ").replace(".", "-")
                listOfClients.append(ClientIp)
    
            for i in range(0,no_of_clients):   
                os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo yum install wget -y'.format(clientspass, listOfClients[i]))
                os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo wget -O /home/hadoop-1.2.1-1.x86_64.rpm https://jokker99.s3.ap-south-1.amazonaws.com/hadoop-1.2.1-1.x86_64.rpm'.format(clientspass, listOfClients[i]))
                os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo wget -O /home/jdk-8u171-linux-x64.rpm https://jokker99.s3.ap-south-1.amazonaws.com/softwares/jdk-8u171-linux-x64.rpm'.format(clientspass, listOfClients[i]))
                print(os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo rpm -ivh /home/jdk-8u171-linux-x64.rpm'.format(clientspass, listOfClients[i])))
                print(os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo rpm -ivh /home/hadoop-1.2.1-1.x86_64.rpm --force'.format(clientspass, listOfClients[i])))
                os.system('ssh -i "{}" ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo wget -O /etc/hadoop/core-site.xml https://jokker99.s3.ap-south-1.amazonaws.com/core-site/core-site.xml'.format(clientspass, listOfClients[i]))
            ##################################
                os.system("aws s3 rm s3://jokker99/core-site/core-site.xml")

            with open('core-site.xml') as f:
                rewrite=f.read().replace(masterIp.replace("-","."),'0.0.0.0')
            with open('core-site.xml', "w") as f:
                f.write(rewrite)
    
          
####################################################### End of hadoop script #########################################################################
######################################################## LVM START #####################################################################            
        elif 'setup l v m' in query:
            print('setup LVM')
            speak("setup L V M")
            print('resize LVM')
            speak("resize L V M")


            if 'setup lvm' in query:
                speak("ENTER YOUR IP Adress")
                ip = input ("ENTER YOUR IP Adress : ")
                os.system("ssh {} sudo fdisk -l".format(ip))
                speak("ENTER YOUR device location")
                disk_location = input("ENTER YOUR device location : ")
                speak("ENTER YOUR volume name")
                vg_name = input("ENTER YOUR volume name : ")
                speak("ENTER YOUR partition size")
                size = input("ENTER YOUR partition size : ")
                speak("ENTER YOUR partition name")
                name = input("ENTER YOUR partition name : ")
                speak("ENTER YOUR location to mount")
                mount = input("ENTER YOUR location to mount : ")
                os.system("ssh {} sudo yum install -y lvm2".format(ip))      
                os.system("ssh {0} sudo pvcreate {1}".format(ip, disk_location))
                os.system("ssh {0} sudo pvdisplay {1}".format(ip, disk_location))
                os.system("ssh {0}  sudo vgcreate {1} {2}".format(ip, vg_name, disk_location))
                os.system("ssh {0}  sudo vgdisplay {1}".format(ip, vg_name))
                os.system("ssh {0} sudo lvcreate --size {1} --name {2}/{3}".format(ip, size, name, vg_name))
                os.system("ssh {0} sudo lvdisplay  {1}/{2}".format(ip, vg_name, name))
                os.system("ssh {} sudo mkfs.ext4 /dev/{}/{}".format(ip, vg_name, name))
                os.system("ssh {} sudo mount /dev/{}/{} {}".format(ip, vg_name, name, mount))

            elif 'resize l v m' in query:
                speak("ENTER YOUR IP Adress")
                ip = input ("ENTER YOUR IP Adress : ")
                speak("Enter size to extend")
                size = input("Enter size to extend : ")
                speak("Enter YOUR partion path")
                lv_path = input("Enter YOUR partion path : ")
                
                os.system("ssh {} sudo fdisk -l".format(ip))
                os.system("ssh {0} sudo lvextend --size {1} {2}".format(ip, size, lv_path))
                os.system("ssh {0} sudo resize2fs {1}".format(ip, lv_path))
            
#########################################  LVM  End #################################################################################
##############################################   Docker Start  ###################################################################3

        elif 'docker' in query:

            speak("enter ip where you want to perform these operations")
            ip = input("enter ip where you want to perform these operations : ")

            os.system('dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo')
            p =['yum install docker-ce --allowerasing --nobest -y','systemctl enable docker','systemctl start docker','docker images']
            for i in p:
                os.system("ssh {} {}".format(ip,i))
            
            speak("Enter Image name")
            osimage = input("Enter Image name : ")
            speak("enter name you want to give to your os")
            osname = input("enter name you want to give to your os : ")
            psid = input("enter id of os : ")
            os.system('ssh {} docker exec   {} yum install python36 -y'.format(ip, id))
            os.system('ssh {} docker exec  {} yum install httpd -y'.format(ip,id))
            os.system('ssh {} docker exec   {} sytemctl start httpd'.format(ip,id))
            os.system('ssh {} docker exec   {}  /usr/sbin/httpd'.format(ip,id))


########################################################  docker ended ########################################################################


        elif 'send mail' in query:
            try:
                speak("Email Please")
                whom = remove(takeCommand())
                speak("What should I say?")
                content = takeCommand()   
                sendEmail(whom, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("There is some issue Try manually")   


###################################################   AWS STARTED   ########################################################################

        elif 'a w s' in query:
            print("................................//Welcome To the Menu Program of AWS//.............................")
            print("Press 1  : To create a key pair")
            print("Press 2  : To delete a key pair")
            print("Press 3  : To create an EBS volume")
            print("Press 4  : To delete an EBS volume")
            print("Press 5  : To create a security group")
            print("Press 6  : To delete a security group")
            print("Press 7  : To Launch your instance")
            print("Press 8  : To attach EBS volume to you instance")
            print("Press 9  : To create S3 bucket")
            print("Press 10 : To delete bucket")
            print("Press 11 : To place object inside S3")
            print("Press 12 : To stop instance")
            print("Press 13 : To start instance")
            print("Press 14 : To terminate instance")
            print()
            P = input("Enter your choice of program")
            print(P)


            if P == '1':
                    print("Enter a key name:- ", end='')
                    key_name = input()
                    os.system("aws ec2 create-key-pair --key-name {}".format(key_name))

            elif P == '2':
                    print("Enter the name of key to be deleted:- ",end='')
                    print("Note that the key will be deleted permanently, if you agree then proceed!!",end='')
                    key_name = input()
                    os.system("aws ec2 delete-key-pair --key-name {}".format(key_name))
                    print("Your desired key has been deleted successfully....")

            elif P == '3':
                    print("Enter the size of the volume size in GB to be created:- ",end='')
                    size = input()
                    print("Enter the availability zone that you wish to choose:- ",end='')
                    AZ = input()
                    os.system("aws ec2 create-volume --availability-zone {} --size {}".format(AZ , size))

            elif P == '4':
                    print("Do you wish to delete the volume?", end='')
                    print("If yes, then type your volume ID", end='')
                    vol_id = input()
                    os.system("aws ec2 delete-volume --volume-id {}".format(vol_id)) 

            elif P == '5':
                    print("Enter the security group name:- ",end='')
                    SG_name = input()
                    print("Enter the description to be given:- ",end='')
                    description = input()
                    print("Enter the VPC Id:- ",end='')
                    VPC_Id = input()
                    os.system("aws ec2 create-security-group --group-name {} --description {} --vpc-id {}".format(SG_name , description , VPC_Id))

            elif P == '6':
                    print("Enter the security group id that you wish to delete:- ",end='')
                    sg_id = input()
                    os.system("aws ec2 delete-security-group --group-id {}".format(sg_id))

            elif P == '7':
                    print("Enter your AMI id for your instance:- ",end='')
                    ami_id = input()
                    print("Enter the type of instance you wish to launch(prefering t2.micro):- ",end='')
                    instance_type = input()
                    print("Enter the count of instances to be launched:- ",end='')
                    count = input()
                    print("Enter your security group ID:- ",end='')
                    SG_ID =input()
                    print("Enter the key to be attached to your instance:- ",end='')
                    key = input()
                    print("Your instance is launching.......")
                    os.system("aws ec2 run-instances --image-id {} --instance-type {} --count {} --security-group-ids {} --subnet-id subnet-5db3f210 --key-name {}".format(ami_id , instance_type , count , SG_ID , key))

            elif P == '8':
                    print("Enter the EBS volume ID to be attached to the instance launched:- ",end='')
                    EBS_ID = input()
                    print("Enter the Instance ID for the volume attaching:- ",end='')
                    Instance_ID = input()
                    os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(EBS_ID , Instance_ID))

            elif P == '9':
                    print("Print a unique bucket name for yourself:- ",end='')
                    Bucket_name = input()
                    print("Enter the region where you wish to create your bucket:- ",end='')
                    region_name = input()
                    os.system("aws s3api create-bucket --bucket {} --region {}".format(Bucket_name , region_name))
                    
            elif P == '10':
                    print("Enter the name of the bucket to be deleted") 
                    Bucket_name = input()
                    print("Enter the region name whose bucket you wish to delete:- ",end='')
                    region_name = input()
                    os.system("aws s3api delete-bucket --bucket {} --region {}".format(Bucket_name , region_name))

            elif P == '11':
                    print("Enter the name of object to be placed inside S3:- ",end='')
                    object_name = input()
                    print("Enter the name of the bucket")
                    Bucket_name = input()
                    os.system("aws s3 cp /root/{} s3://{} --ac1 public-read".format(object_name , Bucket_name))


            elif P == '12':
                    print("Enter the instance Id that you wish to stop:- ",end='')
                    Instance_ID = input()
                    os.system("aws ec2 stop-instances --instance-ids {}".format(Instance_ID))

            elif P == '13':
                    print("Enter the instance id for starting the instance:- ",end='')
                    Instance_ID = input()
                    os.system("aws ec2 start-instances --instance-ids {}".format(Instance_ID))

            elif P == '14':
                    print("Enter the instance id for terminating the instance:- ",end='')
                    Instance_ID = input()
                    os.system("aws ec2 terminate-instances --instance-ids {}".format(Instance_ID))
                    
            else:
                    print("Command not found....")
                    print("Try again")
                    exit()