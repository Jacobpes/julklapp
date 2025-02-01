import random
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# List of people
people = [["Emmi"], ["Evert", "Maria"], ["Jacob", "Amanda"], ["Albert", "Jemina"], ["Juulia", "Junna"], ["Tony"]]

load_dotenv()

email_addresses = {
    "Emmi": "emilia.pesamaa@gmail.com",
    "Evert": "evertpesamaa@gmail.com",
    "Maria": "maicken_@hotmail.com",
    "Jacob": "jacob.pesamaa@gmail.com",
    "Amanda": "amanda.pesamaa@hotmail.com",
    "Albert": "albertlind321@gmail.com",
    "Jemina": "jeminapesamaa@gmail.com",
    "Juulia": "juulia.sulkakoski@gmail.com",
    "Junna": "junna.sulkakoski@gmail.com",
    "Tony": "tonysalin10@gmail.com"
}

# Email configuration
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')

DEBUG = True

# Print out the environment variables to debug
if DEBUG:
    print(f"SMTP_SERVER: {SMTP_SERVER}")
    print(f"SMTP_PORT: {SMTP_PORT}")
print(f"SENDER_EMAIL: {SENDER_EMAIL}")

print("--------------------------------")
print("Agent is running...")
print("")
item_id_memory = []
# read item_id_memory from file of found. item_id_memory.txt separated by commas
if os.path.exists('item_id_memory.txt'):
    with open('item_id_memory.txt', 'r') as file:
        item_id_memory = file.read().split(',')
        file.close()
else:
    item_id_memory = []
    # create item_id_memory.txt
    with open('item_id_memory.txt', 'w') as file:
        file.write('')
    file.close()

def send_email(subject, body, receiver_email, is_html=False):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body with appropriate MIME type
    if is_html:
        msg.attach(MIMEText(body, 'html'))
    else:
        msg.attach(MIMEText(body, 'plain'))

    try:
        # Use SMTP_SSL if port is 465, otherwise use SMTP and starttls
        if SMTP_PORT == '465':
            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
        else:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.ehlo()
                server.starttls()  # Secure the connection
                server.ehlo()
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
        
        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        import traceback
        traceback.print_exc()
        return False



def assign_gifts(people):
    # Create a list of all people
    all_people = [person for pair in people for person in pair]
    # Create a dictionary to keep track of assigned gifts
    gift_assignments = {}

    # Function to check if an assignment is valid
    def is_valid_assignment(giver, receiver):
        # Check if the receiver is the partner of the giver
        for pair in people:
            if giver in pair and receiver in pair:
                return False
        # Check if the receiver has already been assigned a gift
        if receiver in gift_assignments.values():
            return False
        # Check if the receiver is already assigned to give a gift to the giver
        if gift_assignments.get(receiver) == giver:
            return False
        return True

    # Assign gifts
    for giver in all_people:
        possible_receivers = [person for person in all_people if person != giver and is_valid_assignment(giver, person)]
        if not possible_receivers:
            # If there are no valid receivers, restart the assignment process
            return assign_gifts(people)
        receiver = random.choice(possible_receivers)
        gift_assignments[giver] = receiver

    # Send emails
    for giver, receiver in gift_assignments.items():
        subject = "Hemlis från tomteverkstan"
        body = (
            f"<b>Hej {giver}. Jag heter tomtenisse-robot. </b><br>"
            f"<img src='https://ostsvenskahandelskammaren.se/wp-content/uploads/2020/12/Jul.jpg' alt='Small Image' style='width:600px; height:auto;'><br>"
            f"Här får du en hemlighet som inte ens Jacob känner till som har programmerat mig. "
            f"Jag drog lott om vem var och en ska köpa julklapp till, här är din lapp:<br>"
            f"<div style='border: 2px dashed #000; padding: 10px; background-color: #f9f9f9; display: inline-block;'>"
            f"<h1 style='margin: 0;'>{receiver}</h1>"
            f"</div><br>"
            f"Tack för att du hjälper oss med vårt jobb, mvh. tomrenisse-robot, tomteverkstan<br>"
        )
        # Send email to the giver
        giver_email = email_addresses.get(giver)
        if giver_email:
            send_email(subject, body, giver_email, is_html=True)

        # write giver and receiver to item_id_memory.txt
        with open('item_id_memory.txt', 'a') as file:
            file.write(f"{giver} buys for {receiver}\n")
        file.close()

assign_gifts(people)

