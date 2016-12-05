### John Dogan ###
## STATE: COMPLETED  ##
from collections import Counter

'''
MAIN FUNCTION
'''
def main():
    
    win = open("mbox_stats.txt", "w")
    
    win.write("-- MBOX STATS --")
    
    win.write("\n\nNumber of Lines: " + countLines());
    
    win.write("\n\nNumber of Messages: " + countMessage());
    
    win.write("\n\nIPs: " + listIP());
    
    win.write("\n\nMail of Top 3: " + mailofTop3());
    
    win.write("\n\nAverage Body of Messages: " + avgBody());
    
    win.write("\n\nMonthly Stats (Month, Number of Messages): " + monthStats());

'''
COUNT LINES FUNCTION
@param count The number of lines
@return count Returns string value of total amount of lines
'''        
def countLines():
    
    fin = open("mbox.txt", "r")
    
    count = 0;

    for line in fin:
        
        count = count + 1;
        
    return str(count);

'''
COUNT MESSAGES FUNCTION
@param count The number of messages
@return  count Returns string value of total amount of messages
'''    
def countMessage():
    
    fin = open("mbox.txt", "r")
    
    count = 0;
    
    for line in fin:
        
        if "From:" in line:
        
            count = count + 1;
            
    fin.close()
    
    return str(count);

'''
LIST IPs FUNCTION
@param ip The list of all IPs 
@return ip Returns the list of all IPs in mbox.txt
'''    
def listIP():
    
    fin = open("mbox.txt", "r")
    
    ips = []
    
    for line in fin:
        
        if "Received:" in line:
            
            one = line.find("[")
            
            two = line.find("]")
            
            if(one & two != -1):
                
                if(line[one + 1:two] != "unix socket"):
                    
                    ips.append(line[one + 1:two])
    
    ips = list(set(ips))
    
    fin.close()
    
    return str(ips);

'''
LIST E-MAILS OF TOP 3 SENDERS FUNCTION
@param top3 List of top 3 senders
@return top3 Returns the top3 senders in mbox.txt
@return recipients Returns the recipients in mbox.txt
'''
def mailofTop3():
    
    fin = open("mbox.txt", "r")
    
    mails = []
    
    top3 = []
    
    recipients = [];
    
    for line in fin:
        
        if "Author: " in line:
            
            mails.append(line[8:-1])
            
    c = Counter(mails)
    
    mails = c.most_common();
    
    mails = mails[0:3];
    
    for list in range(3):
    
        top3.append(mails[list][0])
        
    fin = open("mbox.txt", "r")
            
    for line in fin:
        
        if "To:" in line:
            
            s = line.split();
            
            recipients.append(s[1])
    
    c = Counter(recipients)
    
    recipients = c.most_common();    
    
    fin.close();
    
    return str(top3) + "\nAll Recipients recieved emails from the same e-mail: " + str(recipients[0][0])

'''
AVG SIZE OF MESSAGE BODY FUNCTION
@param bodies The added bodies of the mbox.txt
@return avgBody Returns the bodies of mbox.txt divided by total message amount.
'''
def avgBody():
    
    fin = open("mbox.txt", "r")
    
    file = fin.readlines();
    
    body = False;
    
    bodies = 0;
    
    messages = countMessage();
    
    for i in range(len(file)):
        
        if "X-DSPAM-Probability: " in file[i]:
            
            body = True;
            
        elif "From" in file[i]:
            
            if len(file[i].split()) ==  7:
                
                body = False;
                
        elif body == True:
            
            bodies = len(file[i]) + bodies;
            
    avgBody = bodies/int(messages)
    
    return str(avgBody);
'''
NUMBER OF MESSAGES SENT FOR EACH MONTH FUNCTION
@param date List of mails sent in the month and year
@return date Returns the amount of mails sent in each month in mbox.txt
'''
def monthStats():
    
    fin = open("mbox.txt", "r")
    
    date = [];
    
    for line in fin:
        
        if "From" in line:
            
            if len(line.split()) ==  7:
            
                s = line.split()
                
                date.append(s[3])
                
    c = Counter(date)
    
    date = c.most_common()
    
    fin.close();

    return str(date)

main()