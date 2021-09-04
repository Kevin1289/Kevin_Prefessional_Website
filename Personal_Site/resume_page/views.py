
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import requests
import os

def home_page(request):
    experiences = {
        'educations':[
            {'name': 'New York University ', 'time': 'Sept 2019 - May 2023', 'program': 'Bachelor of Computer Science, Minor in Finance', 'description': 'My undergraduate studies at NYU revolves around learning advance programming concepts/skills such as Data Structures, Object Oriented Programming and Algorithms. While studying at NYU, I\'ve built a valuable network and took my first steps towards my professional career.', 'link': 'https://www.nyu.edu/'},
            {'name': 'Brooklyn Technical High School', 'time': 'Sept 2015 - Jun 2019', 'program': 'High School Diploma', 'description': 'Highschool is where I made some of the most important decisions of my life. Taking advantage of the major system, I studied mechanical engineering and fell in love with the programming aspect of the courses. While attending this school, I made some of my closest friends and started my first job.', 'link': 'https://www.bths.edu/'}
        ], 
        
    }

    career = [
            {'company': 'Citadel', 'time': '2021 - Present', 'position': 'Data Management Intern / Full Stack Developer', 'location': 'New York, NY', 'description': 'I interned on Citadel\'s Data Management Team, where I built a new website that allows users to update email routing throughout the company. This website greatly reduces the time to update routing from hours to minutes, increasing productivity and decreasing risk throughout the company. Independently built all aspects of the website including front-end, back-end, and database.',  'link': 'https://www.citadel.com/' },
            {'company': 'New York University', 'time': 'Aug 2020 - Present', 'position': 'Web Developer/Teaching Assistant', 'location': 'Brooklyn, NY', 'description': 'As part of the Web-Development Team, I built a new website for the course (used by over 1000 students every year). I also play a leadership role in the classroom setting, introducing students to various concepts and software used in engineering. Supervised and assist students in Semester-Long Design Projects.',  'link': 'https://www.nyu.edu/' },
            {'company': 'New York University', 'time': 'Jan 2021 - May 2021', 'position': 'Smart Wearable Researcher', 'location': 'Brooklyn, NY', 'description': 'Member of NYU’s Smart Wearable Bio-Tracker for In-Home TeleRehab & TeleMonitoring Research Team. We design, implement, and validate a novel bidirectional human-machine interface that detects the motor intent users, and provides biofeedback for augmenting human sensorimotor capacity. I specialize in building the software that analyzes and plots biofeedback signals.',  'link': 'https://www.nyu.edu/' },
            {'company': 'New York University', 'time': 'Sept 2019 - May 2020', 'position': 'Athletic Facility Supervisor', 'location': 'New York, NY', 'description': 'Oversaw the safety of programs at the gym. Verified identity of members and recorded entrance and exit times.',  'link': 'https://www.nyu.edu/' },
            {'company': 'New York University', 'time': 'Sept 2019 - Jan 2020', 'position': 'React Web Developer', 'location': 'New York, NY', 'description': 'Built an app providing NYU students with a safe platform to bond, form study groups, and stay informed on events. Focused on Frontend/UI Development.',  'link': 'https://www.nyu.edu/' },
            {'company': 'Leap Education', 'time': 'Jan 2018 - May 2020', 'position': 'Multi-Subject Teacher', 'location': 'New York, NY', 'description': 'Prepared interactive lessons to facilitate personalized learning for each student. Provided individual structure to lessons to assist grasping of material, graded classwork, and homework, and managed classroom order. ',  'link': 'none' },
            {'company': 'Brooklyn Technical High School - United Nations Awareness Club', 'time': 'Sept 2018 - June 2019', 'position': 'Club President', 'location': 'New York, NY', 'description': 'I founded the club and was responsible for planned and organized meetings. During meetings, members learned about difficulties that are prevalent throughout the world. together, we raised awareness of problems that the United Nations face to our peers.',  'link': 'https://www.bths.edu/' },
            {'company': 'Brooklyn Public Library - Leonard Branch', 'time': 'Sept 2017 - June 2018', 'position': 'T4 Education and Technology Intern', 'location': 'Brooklyn, NY', 'description': 'Provided technology to patrons including personalized technology usage, troubleshooting hardware, and software issues. Conducted programming classes for kids ages 7-12 on coding skills and robotics using LEGO. Supervised and led NYC First Lego Robotics Team which competed in a borough tournament.',  'link': 'https://www.bklynlibrary.org/support/volunteer/t4' }
        ]

    projects = [
        {'image': '/images/personal_website.png', 'image_alt':'Personal Website', 'name': 'Professional Website (Sept 2021)', 'link': 'http://kevinwu.pythonanywhere.com/', 'description': 'Created a Website using Django for others to learn about my story. Used Django\'s built-in python web server. ', 'used': 'Utilized: Python, HTML, CSS.' },
        {'image': '/images/weatherman_logo.png', 'image_alt':'Weatherman', 'name': 'Weatherman', 'link': 'https://weatheruser-ce3d4.web.app/', 'description': 'Launched a platform for adventurists to check the weather by implementing an API. This platform also establishes a community for users to share stories and inspire others.', 'used':' Utilize: React.js, JavaScript, HTML, Firebase, CSS.' },
        {'image': '/images/clique_logo.png', 'image_alt':'Clique Logo', 'name': 'Clique (Aug 2020)', 'link': 'https://github.com/Kevin1289/Clique.io_site', 'description': 'Worked on a team to build a Website to connect students and employers using the Django framework. Performed backend and frontend work and oversaw communication between backend and frontend teams. ', 'used':'Utilized: Python, HTML, CSS, PostgreSQL.' },
        {'image': '/images/mta.png', 'image_alt':'MTA Logo', 'name': 'Train Customer Support System (Sept 2019)', 'link': 'http://127.0.0.1:8000/login/', 'description': 'Developed a program featuring the abilities to explore train stops and to find common train stops, allowing for a easier navigation of NYC\'s complicated train routes. Users are also able to create accounts, where their past searches are saved.', 'used':'Utilized: Python, Django' },
        {'image': '/images/iFeeder_pic.jpg', 'image_alt':'iFeeder', 'name': 'iFeeder - The Automatic Pet Feeder (Sept 2019)', 'link': 'http://127.0.0.1:8000/iFeeder', 'description': 'Played the role of the Chief Hardware Engineer and Chief Designer & Programmer. Designed a self-sufficient, innovative, and cost-efficient product with the ability to dispense food, water, and snacks for a variety of pets. Created professional marketing pitch, prototype, program, advertisement. ', 'used':'Utilized: C++, Autodesk Fusion 360, Arduino IDE, Microsoft Office, Cura, Adobe Illustrator ' },
    ]

    params = (
        ('sign', 'capricorn'),
        ('day', 'today'),
    )
    response = requests.post('https://aztro.sameerkumar.website/', params=params)
    description = response.json()['description']
    return render(request, 'resume_website/resume_page.html', {'description':description, 'experiences': experiences, 'career_recent': career[:3], 'career_old': career[3:], 'projects': projects })

def iFeeder(request):
    return render(request, 'resume_website/iFeeder_Home.html')

def ifeeder_ppt(request):
    return render(request, 'resume_website/ifeeder_ppt.html')

def ifeeder_flowchart(request):
    return render(request, 'resume_website/ifeeder_ppt.html')

def ifeeder_ad(request):
    return render(request, 'resume_website/ifeeder_ppt.html')

# def daily_horoscope(request):
#     params = (
#         ('sign', 'aries'),
#         ('day', 'today'),
#     )
#     response = requests.post('https://aztro.sameerkumar.website/', params=params)
#     return render(request, 'resume_website/resume_page.html', {'response':response})

def train_project(request):
    class train(object):
        def __init__(self, file_name):
            self.file_name = file_name
            self.dict = {}
            self.dict_overlap = []

        def make_line(self, answer):
            final = ""
            with open(self.file_name, "r") as file:
                file.readline()
                for line in file:
                    lst = line.split(",")
                    train = lst[0][0]
                    stop = lst[2]
                    if train not in self.dict:
                        self.dict[train] = stop + ", "
                    elif stop not in self.dict[train]:
                        self.dict[train] += stop + ", "
                for item in self.dict[answer]:
                    final += item
                print(answer, "line: ", final[:-2])

        def make_list(self):
            module_dir = os.path.dirname(__file__)
            file_path = os.path.join(module_dir, 'mta_train_stop_data1.txt')
            with open(file_path, "r") as file:
                file.readline()
                for line in file:
                    lst = line.strip().split(",")
                    train = lst[0][0]
                    stop = lst[2]
                    if train not in self.dict:
                        self.dict[train] = stop + ", "
                    elif stop not in self.dict[train]:
                        self.dict[train] += stop + ", "

        def stop_overlap(self, line1, line2):
            self.make_list()
            count1 = 0
            count2 = 0
            lst1 = self.dict[line1].split(",")
            lst1[0] = ' ' + lst1[0]
            lst2 = self.dict[line2].split(",")
            lst2[0] = ' ' + lst2[0]
            for stop in lst1:
                count2 = 0
                for stop_other in range(len(lst2) - 1):
                    counter = stop_other - 1
                    if lst1[count1] == lst2[count2]:
                        self.dict_overlap.append(stop)
                    count2 += 1
                count1 += 1

            if len(self.dict_overlap) == 0:
                print(
                    "Unfortunately, there are no common stops for these trains. Please try a different set of trains.")
            else:
                sto = ""
                for station in self.dict_overlap:
                    sto += station + " "
                print("The common stops for theses trains are " + sto[:-1] + ".")
                print("Thank you so much for using our service. Have a nice day. \n")
            main()

    def choose_operation():
        print(
            "Enter 'all stops' to display all the stops for a train" + '\n' + "Enter 'common station' to find any common stations between two trains" + '\n' + 'Enter "done" to exit this application.')
        return input()

    def show_stops():
        answer = ("default")
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, 'mta_train_stop_data1.txt')
        while answer != "done":
            print("")
            answer = input("Please enter a train line. If done with this service, please enter 'stop'. ")
            trainoverlap = train(file_path)
            trainoverlap.make_list()
            if answer == 'stop':
                print("Thank you so much for using our service. Have a nice day. \n")
                main()
            train1 = train(file_path)
            if answer not in trainoverlap.dict and answer != "done":
                print("Please enter in a valid train. Thank you.")
                show_stops()
            print("")
            print("")
            train1.make_line(answer)

    def main():
        job = choose_operation()
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, 'mta_train_stop_data1.txt')
        trainoverlap = train(file_path)
        trainoverlap.make_list()
        if job == "all stops":
            show_stops()
        elif job == "common station":
            line1 = input("Enter one of the two trains that you would like to find similiar stations of.")
            while line1 not in trainoverlap.dict:
                print("Please enter in a valid train. Thank you.")
                line1 = input("Enter one of the two trains that you would like to find similiar stations of.")
            print("")
            line2 = input("Enter the second of the two trains that you would like to find similiar stations of.")
            while line2 not in trainoverlap.dict:
                print("Please enter in a valid train. Thank you.")
                line2 = input("Enter one of the two trains that you would like to find similiar stations of.")
            print("")
            trainoverlap = train(file_path)
            trainoverlap.make_list()
            trainoverlap.stop_overlap(line1, line2)
        elif job == 'done':
            return render(request, 'resume_website/resume_page.html')
        else:
            print("please enter a valid choice.")
            main()

    main()
    return render(request, 'resume_website/resume_page.html')

