# Salt Analysis - Project

      
      
## Requirements
1. Works on any python 3.X versions available
2. Internet Connection required for accessing the youtube content



## Structure of the project

1. SaltAnalysisProcedure.py
2. GUI2.py
3. Groupseparation.py
4. Youtube.py
5. acidradicals.py
6. youtubelinks.bin



## Working Principle

1. The file SaltAnalysisProcedure.py holds all the required procedures.
2. The file youtubelinks.bin holds all the youtube video links.


The file **GUI2.py** imports the above 2 files and interacts with the user in the form of a GUI(Graphical User Interface).It contains buttons which are programmed to return the observation, procedure and conclusion of the required salt. As we are doing the systematic salt analysis we also provide the group separation chart. It is obtained from Groupseparation.py.
**GUI2.py** also reads the procedures from the SaltAnalysisProcedure.py for the combined results and it takes the procedure from both **acidradicals.py** and **basicradicals.py** for showing results for both individual procedures of a particular Acid Radical or a Basic radical respectively.
We felt that practical learning is much more efficient than just the theory ( procedures ) , so we also added some youtube links from the channel owned by  AmritaCreate where they perform all the salt analysis practically in the lab . So for doing this we have used **youtubelinks.bin** where we have stored all the links and the  **GUI2.py**
In order to ensure the salt analysis is done accurately , we also have included youtube videos which can help you to do it properly. It is obtained from youtubelinks.txt and  **GUI2.py** will read the links from the text file. We have achieved this by studying and using the Python File Handling Chapter  .



## Bibiliography

1. The youtube videos were sourced from [AmritaCreate](https://www.youtube.com/channel/UCBsy7f40NzuWOhP3YdyyBjA).
  **"Copyright Disclaimer under Section 107 of the copyright act 1976, allowance is made for fair use for purposes such as criticism, comment, news reporting, scholarship, and        research. Fair use is a use permitted by copyright statute that might otherwise be infringing.**
  Due to time constraints we were not able to record the video demonstration and hence we used existing YouTube videos for our project. Which happened to be from [AmritaCreate](https://www.youtube.com/channel/UCBsy7f40NzuWOhP3YdyyBjA).
2. We also referred to the [Python Docs](https://docs.python.org/3.7/).,[Geek for Geeks](https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar)
3. We cleared our doubts from [Stack Overflow](https://stackoverflow.com/).
4. We rediscovered a bug in python whose solution we got from [Python Bugs](https://bugs.python.org/issue36468)
