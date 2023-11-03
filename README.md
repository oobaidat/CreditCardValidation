# Luhn algorithm and credit card validation
### Background Information
In banks around the world, credit card numbers follow one standard algorithm called the Luhn algorithm. Using such an algorithm we can check the validity of the Credit card’s number.\
Luhn algorithm is an algorithm that has been famously related to checking the validity of a credit card number.\
The Luhn algorithm was patented by an IBM scientist, Hans Peter Luhn. The patent was applied for on January 6th, 1954. And officially approved on August 23rd, 1960. Now the patent is described in the U.S. Patent No. 2,950,048.


### The Luhn algorithm
- Start with the far right of the number and double the value of every second digit till the start of the number.
- If after the doubling, a number with two digits is produced, such as numbers that are greater than 9. Then add the digits of the product for example 13: 1+3 = 4. Ending up with a single digit.
- Find the sum of all the digits in the number.
- If the total is divisible by 10, i.e., mod 10 of the sum is equal to 0, then the credit card number is valid, else it is invalid. Hence why the algorithm is sometimes referred to as the mod 10 algorithm.


### Solution
The way to check whether a credit card number was to implement two checks. The first being a very simple one which makes sure that the number starts with the correct digits (4/5/37/6) and has a length between 13 and 16 as all credit card numbers obey those two rules. The second check being the use of the Luhn algorithm. In combination, we will be able to tell the user whether the numbers being generated are valid or not as credit card numbers.


### Approach
How were the tasks split:\
In the project, we have identified several variables related to the problem. We divided the work into mini projects, when combined give us a full solution to the assignment at hand.\
**Research:** Learn about the history of the Luhn algorithm and its uses.\
**Pseudocode:** Write in simple language how to instruct a computer to use the Luhn algorithm and execute the task we were given.\
**Flowchart:** Make a more visual and detailed way of seeing how the data gets processed.\
**Code:** From the pseudocode and flowchart, derive an executable program in python that does what the task needs.\
**Presentation:** Make a presentation with key details to help present how the project went.\
**Video:** Present the project in a quick digestible way.\
**Report:** Written in detail and showing of each step was reached to give a total overview of the project.


### Tools used
To get the results we were able to reach, we had to use multiple tools.\
**WhatsApp:** Used as a main form of communication.\
**Google drive:** Used to make documents and presentations in real-time with teammates.\
**Zoom:** Used infrequently to hold meetings, and to record the video.\
**Search engine:** Used to research the Luhn algorithm and help with coding.\
**Flow.io:** Used to create the flowchart.\
**Visual studio code:** Used to create the code in python.


### Solution strategy
In tackling this project, we had to use multiple solution strategies to reach a solution efficiently and get a good result.\
**Divide and conquer:** In trying to get a good approach to the assignment, we instinctively divided the project into tasks giving each person a chunk and combining them to create a full solution. This was also used for making the code, where we started with pseudocode which is simple going to a flowchart and ending up with a complex code.\
**Mathematical formulas/equations:** The Luhn algorithm is a simple checksum formula. Where using a set of mathematical steps we check a sum with a condition to see whether the number we have is valid or not. By understanding the Luhn algorithm, we translated the steps of the algorithm into code and executed it on the numbers.\
**Trial and error:** While coding many bugs were present, and the main way of finding them was by using trial and error. By testing parts of the code, we get a better understanding of where the error could be. Making the process of coding much smoother.


### Obstacles and solutions
A big issue we had was our pseudocode and flowchart looked very code-like. Having to go through multiple iterations, referring to the slides and previous assignments to arrive at a more abstract version.\
At the start we tried using even and odd positions to execute the Luhn algorithm thinking that makes more sense. But after testing we found out that it does not apply the same way to when if the number being checked was odd or even. So, we had to rewrite the code to be able to work on all kinds of numbers, using iteration from the end of the number. Exactly how the algorithm is described.\
When trying to get the position of a digit in the number, we first tried to find the index of that digit in the number using built in functions in python. However, we realised that when having duplicates this was an issue as by doing that, we always get the index of the first occurrence of that digit in the number. To counteract this, we started using a range derived from the number’s length to better determine the digit’s in question position. (instead of for i in number, we used for i in range(length of number)).\
When generating random credit card numbers, odds of the number being a valid credit card number was very low. To increase the chances of the number being valid, we limited number of digits the generated number can have, allowing the number to have a much higher chance of passing the first check.


## Pseudocode
Generate random number(s), each time displaying the number and the number’s credit card validity to the user by\
&nbsp;&nbsp;&nbsp;&nbsp;Selecting a random digit (0/1/2/3/4/5/6/7/8/9) and combining them to form a number of a random length between 12 and 17\
&nbsp;&nbsp;&nbsp;&nbsp;IF the random number starts with (4/5/37/6) and its length is between 13 and 16\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Going backwards from the randomly generated number starting from the second to last position\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Double every other digit\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sum the digits (the ones and tens) of the doubled digits\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Going backwards from the randomly generated number starting from the last position\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add every other digit to the sum\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF the sum is divisible by 10\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Display “Randomly generated number: <generated number>\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is valid”\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ELSE\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Display “Randomly generated number: <generated number>\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is invalid”\
&nbsp;&nbsp;&nbsp;&nbsp;ELSE\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Display “Randomly generated number: <generated number>\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is invalid”


## Flowchart
![Flowchart](/CreditCardFlow.png)
