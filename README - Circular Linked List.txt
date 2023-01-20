

PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

The problem that you are going to solve is known as Josephus problem and it is stated as follows. There
is a group of soldiers surrounded by an overwhelming enemy force. There is no hope for victory without
reinforcements, so they make a pact to commit suicide.

They form a circle and a number nis picked from a hat. One of their names is picked at random.
Beginning with the soldier whose name is picked, they begin to count clockwise around the circle. When
the count reaches n, that soldier is executed, and the count begins again with the next man. The process
continues so that each time the count reaches n, a man is removed from the circle. Once a soldier is removed
from the circle he is no longer counted. The last soldier remaining was supposed to take his own life.
According to legend the last soldier remaining was Josephus and instead of taking his own life he joined the
enemy forces and survived.

The problem is: given a number n, the ordering of the men in the circle, and the man from whom the
count begins, to determine the order in which the men are eliminated from the circle and which man escapes.
For example, suppose that n equals 3 and there are five men named A, B, C, D, and E. We count three men,
starting at A, so that C is eliminated first. We then begin at D and count D, E, and back to A, so that A is
eliminated next. Then we count B, D, and E (C has already been eliminated) and finally B, D, and B, so that
D is the man who escapes.

You will use a circular linked list. You have worked on the linear linked list in your previous home work.
To make a circular linked list you need to make the next field in the last link of the linked list point back to
the first link instead of being null. From any point in a circular list it is possible to reach any other point in
the list. Thus any link can be the first or last link. One useful convention is to let the external pointer to the
circular list point to the last link and to allow the following link be the first link. We also have the convention
that a null pointer represents an empty circular list.

Instead of giving the soldiers names you will assign them numbers serially starting from 1 (one).

This way you can use the Link class that we discussed. In your program you will read the data from a
file called josephus.in.

1. The first line gives the number of soldiers.
2. The second line gives the soldier from where the counting starts.
3. The third line gives the elimination number.

You will create a circular linked list having the number of soldier specified. Your program will print out
the order in which the soldiers get eliminated.

You will modify the functions insert(), find(), and delete() from the LinkedList class. The main workhorse
of the program will be the delete after() method. This takes the starting Link and the elimination number
n and deletes the nth Link from the starting Link. It returns the data of the deleted Link and the next Link
after the Link that was deleted.

Input:

Suppose the input file was the following:

12
1
3

Output:

Then your output will be:

3
6
9
12
4
8
1
7
2
11
5
10

The last line of your output will be the number of the soldier that escapes.
