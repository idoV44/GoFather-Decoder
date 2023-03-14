<img src="https://github.com/idoV44/GoFather-Decoder/blob/main/Preview.jpg" width="700" >

This is a script made to decode GodFather 'drop' URL. Inside the JAVA file you can find functions whose role is to code a key that will be used to decode the String and thus we will find the 'post' URL and then, we can find the triggers.

The script receives a Telegram URL and returns the Malware triggers. It does this through the following steps:

a. Decoding the functions through the Java code and finding the permanent Key.\
b. Receiving the Telegram URL which contains a String encoded in Base64 format, Blowfish (ECB) and "ABC" as the key.\
c. The script decodes the String and extracts the 'POST' URL that relevant to the malware.\
d. The algorithm will use a list, in order to find the relevant sub-domain. This will be done using an status check that will return Status 200.\
e. The following post data will be sent: Host, country, version and key\
f. The relevant triggers for the malware will be accepted.\
g. A check will be made to see if the URL's are already registered in the system.

