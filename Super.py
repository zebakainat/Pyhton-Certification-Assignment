class Super:
    science_q_e={}
    science_q_h={}
    science_q_m={}
    maths_q_e={}
    maths_q_h={}
    maths_q_m={}
    options={}
    s_user={}
    def __init__(self,s_id,s_name):
        self.s_id=s_id
        self.s_names=s_name
        self.All_Topic={}
        print("hey",s_name,"you can set/edit/view a quiz")

    def add_question(self):
        while True:
            quiz=input("Do you want to set quiz on some other topic?(y/n)")
            if (quiz.lower()=='y'):
                topic=input("Enter the topic you want to set the quiz on (science/maths):")
                difficulty=input("\nEnter the difficulty level of quiz(easy/hard/medium):")

                if topic.lower()=="science" and difficulty.lower()=="easy":
                    no_of_q=int(input("\nHow many questions you want to set:"))
                    for val in range(no_of_q):
                        question=input("\nEnter the question:")
                        opt=input("\nEnter your options seperated by space:").split()
                        Super.options[question]=opt
                        answer=input("\nEnter the answer:")
                        Super.science_q_e[question]=answer

                elif topic.lower()=='science' and difficulty.lower()=="hard":
                    no_of_q=int(input("\nHow many questions you want to set:"))
                    for val in range(no_of_q):
                        question=input("\nEnter the question")
                        opt=input("\nEneter your options seperated by space:").split()
                        Super.options[question]=opt
                        answer=input("\nEnter the answer:")
                        Super.science_q_h[question]=answer

                elif topic.lower()=='science' and difficulty.lower()=="medium":
                    no_of_q=int(input("\nHow many questions you want to set:"))
                    for val in range(no_of_q):
                        question=input("\nEnter the question")
                        opt=input("\nEneter your options seperated by space:").split()
                        Super.options[question]=opt
                        answer=input("\nEnter the answer:")
                        Super.science_q_m[question]=answer

                elif topic.lower()=='maths' and difficulty.lower()=="easy":
                    no_of_q=int(input("\nHow many questions you want to set:"))
                    for val in range(no_of_q):
                        question=input("\nEnter the question:")
                        opt=input("\nEnter your options seperated by space:").split()
                        Super.options[question]=opt
                        answer=input("\nEnter the answer:")
                        Super.maths_q_e[question]=answer

                elif topic.lower()=='maths' and difficulty.lower()=="medium":
                    no_of_q=int(input("\nHow many questions you want to set:"))
                    for val in range(no_of_q):
                        question=input("\nEnter the question:")
                        opt=input("\nEnter your options seperated by space:").split()
                        Super.options[question]=opt
                        answer=input("\nEnter the answer:")
                        Super.maths_q_m[question]=answer

                elif topic.lower()=='maths' and difficulty.lower()=="hard":
                    no_of_q=int(input("\nHow many questions you want to set:"))
                    for val in range(no_of_q):
                        question=input("\nEnter the question:")
                        opt=input("\nEnter your options seperated by space:").split()
                        Super.options[question]=opt
                        answer=input("\nEnter the answer:")
                        Super.maths_q_h[question]=answer
                else:
                    break
            else:
                break

    def edit_question(self):
        while True:
            add_q=input("Do you want to add question(y/n)")
            if add_q.lower()=='y':
                topic=input("Enter the topic where you want your question to be added (science/maths):")
                difficulty=input("\nEnter the difficulty level of the question (easy/hard/medium):")

                if topic.lower()=='science' and difficulty.lower()=='easy':
                    question=input("\nEnter the question:")
                    opt=input("\nEnter your options seperated by space:").split()
                    Super.options[question]=opt
                    answer=input("\nEnter the answer:")
                    Super.science_q_e[question]=answer

                elif topic.lower()=='science' and difficulty.lower()=="hard":
                    question=input("\nEnter the question")
                    opt=input("\nEnter your options seperated by space:").split()
                    Super.options[question]=opt
                    answer=input("\nEnter the answer:")
                    Super.science_q_h[question]=answer

                elif topic.lower()=='science' and difficulty.lower()=="medium":
                    question=input("\nEnter the question")
                    opt=input("\nEnter your options seperated by space:").split()
                    Super.options[question]=opt
                    answer=input("\nEnter the answer:")
                    Super.science_q_m[question]=answer

                elif topic.lower()=='maths' and difficulty.lower()=="easy":
                    question=input("\nEnter the question:")
                    opt=input("\nEnter your options seperated by space:").split()
                    Super.options[question]=opt
                    answer=input("\nEnter the answer:")
                    Super.maths_q_e[question]=answer

                elif topic.lower()=='maths' and difficulty.lower()=="medium":
                    question=input("\nEnter the question:")
                    opt=input("\nEnter your options seperated by space:").split()
                    Super.options[question]=opt
                    answer=input("\nEnter the answer:")
                    Super.maths_q_m[question]=answer


                elif topic.lower()=='maths' and difficulty.lower()=="hard":
                    question=input("\nEnter the question:")
                    opt=input("\nEnter your options seperated by space:").split()
                    Super.options[question]=opt
                    answer=input("\nEnter the answer:")
                    Super.maths_q_h[question]=answer
            else:
                break

    def view_questions(self): 
        quiz=input("\nDo you want to see the questions?(y/n)")
        if (quiz.lower()=='y'):
                for i in Super.maths_q_e.keys():
                    print(i)
                for i in Super.maths_q_m.keys():
                    print(i)
                for i in Super.maths_q_h.keys():
                    print(i)
                for i in Super.science_q_e.keys():
                    print(i)
                for i in Super.science_q_m.keys():
                    print(i)
                for i in Super.science_q_h.keys():
                    print(i)

    def delete_questions(self):
        quiz=input("\nDo you want to delete the questions?(y/n)\n")
        if (quiz.lower()=='y'):
            del Super.maths_q_e
            del Super.maths_q_m
            del Super.maths_q_h
            del Super.science_q_e
            del Super.science_q_m
            del Super.science_q_h

    def create_topic(self):
        keys_len=list(self.All_Topic.keys())
        how_many_topic=int(input("\n Enter the no of topic you want to create: "))
        length_of_key=len(keys_len)
        last=length_of_key+how_many_topic
        
        for i in range(length_of_key+1,last+1):
            self.All_Topic[i]=input("\n Enter topic name: ")

    def view_topic(self):
        for value in self.All_Topic:
            print(str(value)+'.',self.All_Topic[value],'\n')

    def edit_topic(self):
        for value in self.All_Topic:
            print(str(value)+'.',self.All_Topic[value])
        topic_no=int(input("\n Enter the topic no you want to edit"))
        self.All_Topic[topic_no]=input("\n Enter topic name: ")

    def delete_topic(self):
        del self.All_Topic

                
                    




               
                




