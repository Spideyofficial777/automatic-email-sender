import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import threading
from flask import Flask

app = Flask(__name__)

EMAIL_ADDRESS = 'vigneshmudhale777@gmail.com'
EMAIL_PASSWORD = 'yillyowmajucuagr'

recipient_list = [
    'support@dbatu.ac.in',
    'dbatu_suport@unisuite.in',
    'acoe_engg@dbatu.ac.in',
    'exam@dbatu.ac.in',
    'smpore@dbatu.ac.in'
]

subject = "MSI पोर्टलवरील चुकीची बॅकलॉग माहिती व फी संदर्भातील अडचण – विनंती"

body = """

आदरणीय परीक्षा नियंत्रक महोदय/महोदया,
सप्रेम नमस्कार,

मी विघ्नेश सिद्धू मुधाळे, द्वितीय वर्ष बी.टेक (इलेक्ट्रॉनिक्स व टेलिकम्युनिकेशन) शाखेचा विद्यार्थी आहे. माझा PRN क्रमांक 23062171372016 असून मी Ashokrao Mane Group of Institutions, वाठार तर्फ वडगाव, कोल्हापूर या महाविद्यालयात शिकतो.
माझ्या तिसऱ्या सत्रामध्ये चार विषयांत बॅकलॉग होती, त्यापैकी मी Remedial परीक्षेद्वारे दोन विषय उत्तीर्ण केले आहेत. मात्र, नवीन MSI पोर्टलवर आजही सर्व चार विषय बॅकलॉग म्हणून दर्शवले जात आहेत, त्यामुळे मला Remedial परीक्षेचा फॉर्म लॉगिनमध्ये दिसत नाही आणि Supplementary फॉर्ममध्ये ₹1200 सर्व चार विषयांसाठी शुल्क आकारले जात आहे, जरी केवळ दोनच विषय बाकी असले तरी.
मागील Remedial परीक्षेच्या वेळी माझ्या लॉगिनमध्ये कोणताही फॉर्म दिसत नव्हता, त्यामुळे मी त्या वेळेस फॉर्म भरू शकलो नाही, आणि शुल्कही भरले गेले नव्हते. सध्या मी मागील वेळचे ₹600 Remedial शुल्कही भरतोय, जे आता घेतले जात आहे.

त्यामुळे माझ्या विनंत्या खालीलप्रमाणे:
1. Remedial व Supplementary परीक्षेच्या शुल्काचे योग्य प्रकारे विभाजन (₹600 + ₹600) करण्यात यावे, व याची स्पष्ट नोंद केली जावी.
2. माझ्या कॉलेजने स्पष्टपणे सांगितले आहे की, "जे विषय उत्तीर्ण झाले आहेत त्यांचे फॉर्म भरू नयेत", म्हणून मी त्या दोन विषयांसाठी परीक्षेला बसणार नाही, याची नोंद घ्यावी.
3. जर मी ₹1200 भरले, तर त्यानंतर उत्तीर्ण झालेले दोन विषय भविष्यात बॅकलॉग म्हणून दर्शवले जाणार नाहीत, याची लेखी खात्री (email/पत्राद्वारे) द्यावी.
4. माझी मागील वेळची अडचण (फॉर्म न दिसल्यामुळे शुल्क न भरू शकणे) लक्षात घेऊन Remedial व Supplementary परीक्षा यामध्ये माझे दोन-दोन विषय विभाजित करावेत.
5. कृपया या अर्जावर १८ जुलै २०२५ पूर्वी निर्णय घेण्यात यावा, जेणेकरून मला न घाबरता पुढील कारवाई करता येईल व परीक्षेला बसता येईल.

मी सर्व शुल्क भरण्यास तयार आहे, परंतु मला भविष्यात कोणतीही गैरसमज किंवा अन्याय होऊ नये यासाठी स्पष्टता व शाश्वती हवी आहे.

आपल्या सहकार्याबद्दल मन:पूर्वक आभारी आहे.

आपला नम्र,

विघ्नेश सिद्धू मुधाळे  
द्वितीय वर्ष बी.टेक (इ. & टि.सी.)  
PRN: 23062171372016  
Ashokrao Mane Group of Institutions (AMGOI),  
वाठार तर्फ वडगाव, ता. हातकणंगले, जि. कोल्हापूर  
मो.: 8483005353  
ईमेल: vigneshmudhale777@gmail.com


✅ Disclaimer (Notice):
🌐 This is an automated email. Please pay immediate attention to the following points.
🛑 If timely action is not taken on this issue, the bot will not be stopped and will continue sending emails repeatedly.
🙏 I sincerely apologize for taking this step. Given the current situation, I had no other option, which is why I was compelled to take this action. Please view this matter with understanding and take the necessary steps.

Without your reply this bot is the not stopend 
"""
DOCUMENT_DIR = "documents"

document_paths = [
    os.path.join(DOCUMENT_DIR, "BTBS301 Engineering Mathematics-III.csv"),
    os.path.join(DOCUMENT_DIR, "BTEXC302 Electronic Devices & Circuits.csv"),
    os.path.join(DOCUMENT_DIR, "Not showing the remedial form 3rd sem .jpg")
]


def send_email():
    for recipient in recipient_list:
        try:
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            for doc_path in document_paths:
                if os.path.exists(doc_path):
                    with open(doc_path, "rb") as f:
                        part = MIMEApplication(f.read(), Name=os.path.basename(doc_path))
                        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(doc_path)}"'
                        msg.attach(part)
                else:
                    print(f"⚠️ File not found: {doc_path}")

            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())

            print(f"✅ Email sent to {recipient}")
        except Exception as e:
            print(f"❌ Failed to send email to {recipient}: {e}")

# Schedule every 1800 seconds (30 min)
schedule.every(1800).seconds.do(send_email)

def scheduler_loop():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start scheduler in background thread
threading.Thread(target=scheduler_loop, daemon=True).start()

@app.route('/')
def home():
    return "📧 Auto Email Sender is Running on Koyeb with Port 8080"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
