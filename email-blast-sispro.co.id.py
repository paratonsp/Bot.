import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from dhooks import Webhook, Embed
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def getHtml(url):
    ua = UserAgent()
    header = {'user-agent':ua.random}
    response = requests.get(url,timeout=3000)
    response.raise_for_status()
    return response.content


with open('C:/Users/parat/Desktop/email-sub-kontraktor.txt','r') as fd:
    for i, line in enumerate(fd.readlines()):

        email = line.strip()
           
        mail_content = """\
        <html>
        <body yahoo="fix" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
            <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0" bgcolor="#505052"
            style="background:#505052;">
            <tr>
                <td align="center" valign="top">

                <!--Logo Part Start-->

                <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
                    <tr>
                    <td align="center" valign="top">
                        <table width="100%" border="0" cellspacing="0" cellpadding="0" class="main">
                        <tr>
                            <td align="center" valign="top" bgcolor="#FFFFFF">
                            <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0" class="two-left-inner">
                                <tr>
                                <td height="35" align="center" valign="top" style=" font-size:35px;line-height:35px;">&nbsp;
                                </td>
                                </tr>
                                <tr>
                                <td align="center" valign="top">
                                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                    <tr>
                                        <td width="50%" align="center" valign="top" class="two-left">
                                        <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
                                            <tr>
                                            <td height="2" style="font-size:2px; line-height:2px;">&nbsp;</td>
                                            </tr>
                                            <tr>
                                            <td align="center" valign="top"
                                                style="font-family:'Open Sans', sans-serif, Verdana; font-size:16px; color:#36373a; font-weight:normal;"
                                                mc:edit="nm-02">
                                                <multiline>call us :<b><a href="#" style="color:#36373a; text-decoration:none;">
                                                    082170252366</a></b></multiline>
                                            </td>
                                            </tr>
                                            <tr>
                                            <td height="35" align="center" valign="top"
                                                style=" font-size:35px;line-height:35px;">&nbsp;</td>
                                            </tr>
                                        </table>
                                        </td>
                                        <td width="50%" align="center" valign="top" class="two-left">
                                        <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
                                            <tr>
                                            <td height="3" style="font-size:3px; line-height:3px;">&nbsp;</td>
                                            </tr>
                                            <tr>
                                            <td align="center" valign="top"
                                                style="font-family:'Open Sans', sans-serif, Verdana; font-size:14px; color:#36373a; font-weight:bold;"
                                                mc:edit="nm-04">
                                                <multiline><a href="#" style="color:#36373a; text-decoration:none;">Surya Indo Makmur</a>.</multiline>
                                            </td>
                                            </tr>
                                            <tr>
                                            <td height="35" align="center" valign="top"
                                                style=" font-size:35px;line-height:35px;">&nbsp;</td>
                                            </tr>
                                        </table>
                                        </td>
                                    </tr>
                                    </table>
                                </td>
                                </tr>
                            </table>
                            </td>
                        </tr>
                        </table>
                    </td>
                    </tr>
                </table>

                <!--Logo Part End-->

                <!--Service Title Part Start-->

                <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
                    <tr>
                    <td align="center" valign="top">
                        <table width="100%" border="0" cellspacing="0" cellpadding="0" class="main">
                        <tr>
                            <td align="center" valign="top" bgcolor="#56ba56">
                            <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0" class="two-left-inner">
                                <tr>
                                <td height="80" align="left" valign="top" style="font-size:80px; line-height:80px;">&nbsp;</td>
                                </tr>
                                <tr>
                                <td align="center" valign="top">
                                    <table width="100%" border="0" align="left" cellpadding="0" cellspacing="0">
                                    <tr>
                                        <td align="center" valign="top"
                                        style="font-family:'Open Sans', sans-serif, Verdana; font-size:22px; color:#FFF; font-weight:normal;"
                                        mc:edit="nm-06">
                                        <multiline>Electrical & Mechanical, Panel Maker</multiline>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td height="5" align="left" valign="top" style="font-size:5px; line-height:5px;">&nbsp;
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="center" valign="top"
                                        style="font-family:'Open Sans', sans-serif, Verdana; font-size:32px; color:#FFF; font-weight:bold;"
                                        mc:edit="nm-07">
                                        <multiline>SURYA INDO MAKMUR</multiline>
                                        </td>
                                    </tr>
                                    </table>
                                </td>
                                </tr>
                                <tr>
                                <td height="80" align="left" valign="top" style="font-size:80px; line-height:80px;">&nbsp;</td>
                                </tr>
                            </table>
                            </td>
                        </tr>
                        </table>
                    </td>
                    </tr>
                </table>

                <!--Service Title Part End-->

                <!--Service List Part Start-->

                <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
                    <tr>
                    <td align="center" valign="top">
                        <table width="100%" border="0" cellspacing="0" cellpadding="0" class="main">
                        <tr>
                            <td align="center" valign="top" bgcolor="#FFFFFF">
                            <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0" class="two-left-inner">

                                <tr>
                                <td height="40" align="center" valign="middle" style="font-size:120px; line-height:40px;">
                                    &nbsp;</td>
                                </tr>

                                <tr>
                                <td align="center" valign="middle">
                                    <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
                                    <tr>

                                        <td width="100%" align="left" valign="top" class="two-left">
                                        <table width="100%" border="0" align="left" cellpadding="0" cellspacing="0">
                                            <tr>
                                            <td align="center" valign="top"
                                                style="font-family:Roboto, 'Open Sans'; font-size:20px; color:#5f5e5e; line-height:38px; font-weight:normal;"
                                                mc:edit="nm-09">
                                                <multiline>Kapasitor Bank</multiline>
                                            </td>
                                            </tr>
                                            <tr>
                                            <td align="center" valign="top"
                                                style="font-family:Roboto, 'Open Sans'; font-size:20px; color:#5f5e5e; line-height:38px; font-weight:normal;"
                                                mc:edit="nm-09">
                                                <multiline>Panel Auto Transfer Switch (ATS)</multiline>
                                            </td>
                                            </tr>
                                            <tr>
                                            <td align="center" valign="top"
                                                style="font-family:Roboto, 'Open Sans'; font-size:20px; color:#5f5e5e; line-height:38px; font-weight:normal;"
                                                mc:edit="nm-09">
                                                <multiline>Panel Auto Main Failure (AMF)</multiline>
                                            </td>
                                            </tr>
                                            <tr>
                                            <td align="center" valign="top"
                                                style="font-family:Roboto, 'Open Sans'; font-size:20px; color:#5f5e5e; line-height:38px; font-weight:normal;"
                                                mc:edit="nm-09">
                                                <multiline>Panel Sinkron Genset</multiline>
                                            </td>
                                            </tr>
                                            <tr>
                                            <td align="center" valign="top"
                                                style="font-family:Roboto, 'Open Sans'; font-size:20px; color:#5f5e5e; line-height:38px; font-weight:normal;"
                                                mc:edit="nm-09">
                                                <multiline>
                                                Panel Medium Voltage Main Distribution (MVMDP)</multiline>
                                            </td>
                                            </tr>
                                            <tr>
                                            <td align="center" valign="top"
                                                style="font-family:Roboto, 'Open Sans'; font-size:20px; color:#5f5e5e; line-height:38px; font-weight:normal;"
                                                mc:edit="nm-09">
                                                <multiline>
                                                Panel Low Voltage Main Distribution (LVMDP)</multiline>
                                            </td>
                                            </tr>
                                            <tr>
                                            <td align="center" valign="top"
                                                style="font-family:Roboto, 'Open Sans'; font-size:20px; color:#5f5e5e; line-height:38px; font-weight:normal;"
                                                mc:edit="nm-09">
                                                <multiline>Panel Sub Distribution (SDP)</multiline>
                                            </td>
                                            </tr>
                                            <tr>
                                            <td align="center" valign="top"
                                                style="font-family:Roboto, 'Open Sans'; font-size:20px; color:#5f5e5e; line-height:38px; font-weight:normal;"
                                                mc:edit="nm-09">
                                                <multiline>Panel Penerangan</multiline>
                                            </td>
                                            </tr>
                                            <tr>
                                            <td align="center" valign="top"
                                                style="font-family:Roboto, 'Open Sans'; font-size:20px; color:#5f5e5e; line-height:38px; font-weight:normal;"
                                                mc:edit="nm-09">
                                                <multiline>Panel Kontrol Genset</multiline>
                                            </td>
                                            </tr>
                                            <tr>
                                            <td align="center" valign="top"
                                                style="font-family:Roboto, 'Open Sans'; font-size:20px; color:#5f5e5e; line-height:38px; font-weight:normal;"
                                                mc:edit="nm-09">
                                                <multiline>Panel Inverter</multiline>
                                            </td>
                                            </tr>
                                            <tr>
                                            <td align="center" valign="top"
                                                style="font-family:Roboto, 'Open Sans'; font-size:20px; color:#5f5e5e; line-height:38px; font-weight:normal;"
                                                mc:edit="nm-09">
                                                <multiline>Panel Motor Dol Starter</multiline>
                                            </td>
                                            </tr>
                                            <tr>
                                            <td align="center" valign="top"
                                                style="font-family:Roboto, 'Open Sans'; font-size:20px; color:#5f5e5e; line-height:38px; font-weight:normal;"
                                                mc:edit="nm-09">
                                                <multiline>Panel Star Delta</multiline>
                                            </td>
                                            </tr>
                                            <tr>
                                            <td align="center" valign="top"
                                                style="font-family:Roboto, 'Open Sans'; font-size:20px; color:#5f5e5e; line-height:38px; font-weight:normal;"
                                                mc:edit="nm-09">
                                                <multiline>Panel Motor Kontrol</multiline>
                                            </td>
                                            </tr>
                                            <tr>
                                            <td align="center" valign="top"
                                                style="font-family:Roboto, 'Open Sans'; font-size:20px; color:#5f5e5e; line-height:38px; font-weight:normal;"
                                                mc:edit="nm-09">
                                                <multiline>Panel Programmable Logic Control (PLC)</multiline>
                                            </td>
                                            </tr>
                                            <tr>
                                            <td align="center" valign="top"
                                                style="font-family: 'Open Sans', sans-serif, Verdana; font-size:14px; line-height:28px; color:#4f8af9; font-weight:bold; text-transform:none;">
                                                &nbsp;</td>
                                            </tr>
                                            <tr>
                                            <td align="center" valign="top">&nbsp;</td>
                                            </tr>
                                        </table>
                                        </td>

                                    </tr>
                                    </table>
                                </td>
                                </tr>

                            </table>
                            </td>
                        </tr>
                        </table>
                    </td>
                    </tr>
                </table>

                <!--Service List Part End-->


                <!--Footer Text Part Start-->

                <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
                    <tr>
                    <td align="center" valign="top">
                        <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0" class="main">
                        <tr>
                            <td align="center" valign="top" bgcolor="#56ba56">


                            <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0" class="main">
                                <tr>
                                <td width="33%" align="left" valign="top" class="two-left">
                                    <table width="100%" border="0" align="left" cellpadding="0" cellspacing="0">
                                    <tr>
                                        <td height="60" align="left" valign="top" style="font-size:60px; line-height:60px;">&nbsp;
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="center" valign="top">&nbsp;</td>
                                    </tr>
                                    <tr>
                                        <td align="left" valign="top"
                                        style="font-family:'Open Sans', sans-serif, Verdana; font-size:13px; font-weight:bold; color:#FFF; text-transform:none;"
                                        mc:edit="nm-87">
                                        <multiline>Call Us</multiline>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="left" valign="top"
                                        style="font-family:'Open Sans', sans-serif, Verdana; font-size:14px; font-weight:normal; color:#FFF; line-height:26px;"
                                        mc:edit="nm-88">
                                        <multiline>0821-7025-2366</multiline>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td height="60" align="left" valign="top" style="font-size:60px; line-height:60px;">&nbsp;
                                        </td>
                                    </tr>
                                    </table>
                                </td>
                                <td width="33%" align="left" valign="top" class="two-left">
                                    <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
                                    <tr>
                                        <td height="60" align="left" valign="top" style="font-size:60px; line-height:60px;">&nbsp;
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="center" valign="top">&nbsp;</td>
                                    </tr>
                                    <tr>
                                        <td align="center" valign="top"
                                        style="font-family:'Open Sans', sans-serif, Verdana; font-size:13px; font-weight:bold; color:#FFF; text-transform:none;"
                                        mc:edit="nm-90">
                                        <multiline>Our Location</multiline>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="center" valign="top"
                                        style="font-family:'Open Sans', sans-serif, Verdana; font-size:14px; font-weight:normal; color:#FFF; line-height:26px;"
                                        mc:edit="nm-91">
                                        <multiline>Jl. Sawahan Sarimulyo 2A, Surabaya, Indonesia.</multiline>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td height="60" align="left" valign="top" style="font-size:60px; line-height:60px;">&nbsp;
                                        </td>
                                    </tr>
                                    </table>
                                </td>
                                <td width="33%" align="left" valign="top" class="two-left">
                                    <table width="100%" border="0" align="left" cellpadding="0" cellspacing="0">
                                    <tr>
                                        <td height="60" align="left" valign="top" style="font-size:60px; line-height:60px;">&nbsp;
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="center" valign="top">&nbsp;</td>
                                    </tr>
                                    <tr>
                                        <td align="right" valign="top"
                                        style="font-family:'Open Sans', sans-serif, Verdana; font-size:13px; font-weight:bold; color:#FFF; text-transform:none;"
                                        mc:edit="nm-93">
                                        <multiline>Mail Us</multiline>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="right" valign="top"
                                        style="font-family:'Open Sans', sans-serif, Verdana; font-size:14px; font-weight:normal; color:#FFF; line-height:26px;"
                                        mc:edit="nm-94">
                                        <multiline>makmur8@gmail.com</multiline>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td height="60" align="left" valign="top" style="font-size:60px; line-height:60px;">&nbsp;
                                        </td>
                                    </tr>
                                    </table>
                                </td>
                                </tr>
                            </table>
                            </td>
                        </tr>
                        </table>
                    </td>
                    </tr>
                </table>

                <!--Footer Text Part End-->

                <!--Copyright Part Start-->

                <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
                    <tr>
                    <td align="center" valign="top">
                        <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0" class="main">
                        <tr>
                            <td align="center" valign="top" bgcolor="#f5f5f5">
                            <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0" class="two-left-inner">
                                <tr>
                                <td height="35" colspan="3" align="center" valign="top"
                                    style="line-height:35px; font-size:35px;">&nbsp;</td>
                                </tr>
                                <tr>
                                <td width="300" height="38" align="left" valign="top" class="two-left"
                                    style="font-family:'Open Sans', sans-serif, Verdana; font-size:14px; font-weight:normal; color:#262626;"
                                    mc:edit="nm-95">
                                    <multiline>Copyright &copy; 2022 Surya Indo Makmur.</multiline>
                                </td>
                                </tr>
                                <tr>
                                <td height="35" colspan="3" align="center" valign="top"
                                    style="line-height:35px; font-size:35px;">&nbsp;</td>
                                </tr>
                            </table>
                            </td>
                        </tr>
                        </table>
                    </td>
                    </tr>
                </table>

                <!--Copyright Part End-->

                </td>
            </tr>
            </table>
        </body>
        </html>
        """

        sender_address = 'promotion.suryaindomakmur@gmail.com'
        sender_pass = 'suryaindomakmur'
        receiver_address = email

        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Electrical & Mechanical, Panel Maker Surabaya'

        message.attach(MIMEText(mail_content, 'html'))

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent to ' + email)


