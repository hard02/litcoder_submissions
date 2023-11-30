
Time Stamp Archive:

You are tasked with designing a Time Travelers Archive system that allows travelers to store and retrieve valuable information from different time periods. The system should support storing key-value pairs associated with specific timestamps and efficiently retrieving the latest value for a given key based on a timestamp.

Design a TimeTravelersArchive class to implement the required functionality:

    Store(string key, string value, int timestamp): This method should store the key keywith the value value at the given timestamp.
    Retrieve(string key, int timestamp): This method should return the latest value
    associated with the key key that has a timestamp less than or equal to the given timestamp.
    If there is no such value found, it should return the output as empty .
    When you retrieve the data, if call wrong method it should print "Wrong method called, please call Store or Retrieve method"

			For Ex: Store language Latin 500
				Store language Old_English 1000
				Retrieve language asa 

Your task is to design the TimeTravelersArchive class and its methods to efficiently handle the storage and retrieval of information across different time periods.
The overall run time complexity should be O(1) for Store and O(log n) for the Retrieve method.

Exercise-1
TimeTravelersArchive archive = new TimeTravelersArchive();
archive.Store(language,Latin,1);
archive.Store(language,Old_English, 2);
string result1 = archive.Retrieve(language;, 1); // Output: Latin;
string result2 = archive.Retrieve(language, 3); // Output: Old English;
string result3 = archive.Retrieve(language, 0); // Output: empty;

Explanation:
First call to retrieve method return Latin as the timestamp is equal to what is passed in the Retrieve call.
Second call returns Old English; as the timestamp of that item is less than the  3 timestamp passed in the Retrieve call.
Third call returns an empty string since there is no timestamp stored which is less than or equal to 0.

Constraints:

    All key/value strings are lowercase.
    The input timestamp for Store and Retrieve method is in the range [1, 10^7].
    The number of calls to the Retrieve method will be less than or equal to 10^4.
    The number of calls to the Store method will be less than or equal to 10^4.

Important Note: Ensure that you save your solution before progressing to the next question and  before submitting your answer.

Exercise -1
Input:
Store key1 value1 1		     //Call to Store method
Store key1 value2 2	    	//Call to Store method
Retrieve key1 1		           //Call to Retrieve method
Retrieve key1 3		          //Call to Retrieve method
Retrieve key1 0		          //Call to Retrieve method

Output:
value1
value2
empty

Exercise - 2
Input:
Store key1 value1 1
Store key1 value2 2
Store key2 value1 3
Store key1 value3 4
Store key2 value2 5
Retrieve key1 1
Retrieve key2 5
Retrieve key1 10

Output:
value1
value2
value3

Exercise - 3
Input:
Store language Latin 10
Store language Old_English 50
Store language Middle_English 90
Store language2 Middle_English 90
Store language1 Latin 190
Store language3 Latin 5
Store language1 Middle_English 20
Retrieve language 2
Retrieve language1 200
Retrieve language3 60
Retrieve language 90

Output:
empty
Middle_English
Latin
Middle_English

