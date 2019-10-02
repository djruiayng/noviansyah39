#===*NIAR TEAM BOT*===#
# -*- coding: utf-8 -*- #

from linepy import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import ChatRoomAnnouncement
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback
from gtts import gTTS
from googletrans import Translator
from threading import Thread,Event
import wikipedia as wiki
requests.packages.urllib3.disable_warnings()
#================================================================================================================================================================================================================================================================================================
print ("[ INFO ] LOGIN")
print ("")
print ("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄")
print ("//==================================\\")
print (" NIAR TEAM BOT")
print (" D.Noviansyah|ID Line : noviansyah39")
print ("\\==================================//")
print ("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄")
print ("")
#================================================================================================================================================================================================================================================================================================
cl = LINE("Email","Password") #Login Email
cl.log("Auth Token : " + str(cl.authToken))

oepoll = OEPoll(cl)
call = cl
creator = ["u76933991bf8d8222f65528498e861189"]
owner = ["u76933991bf8d8222f65528498e861189"]
admin = ["u76933991bf8d8222f65528498e861189"]
staff = ["u76933991bf8d8222f65528498e861189"]

lineProfile = cl.getProfile()
mid = cl.getProfile().mid
Bots = [mid]
Saints = admin + owner + staff
Team = creator + owner + admin + staff + Bots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)


welcome = []
targets = []
userTemp = {}
userKicked = []
msg_dict = {}
msg_dict1 = {}
dt_to_str = {}
temp_flood = {}
groupName = {}
groupImage = {}
list = []
ban_list = []
offbot = []


settings = {
    "autoBlock": False,
    "autoRead": False,
    "welcome": False,
    "leave": False,
    "mid": False,
    "keyCommand": "dent",
    "commentPost": "Auto Like & Comment : NIAR TEAM BOT",
    "replySticker": False,
    "stickerOn": False,
    "checkContact": False,
    "postEndUrl": True,
    "checkPost": False,
    "setKey": False,
    "restartPoint": False,
    "checkSticker": False,
    "userMentioned": False,
    "listSticker": False,
    "messageSticker": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }, 
    "unsendMessage": False,
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "autoJoinTicket":False,
    "SpamInvite":False,
    "displayName": "",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}

wait = {
    "limit": 2,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "dhenza":{},
    "likeOn": True,
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoCancel':{"on":True, "members":1},
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "unsend":True,
    "selfbot":True,
    "mention":"Hayooo Ketahuan Ngintip...\nSini Masuk Kak, Ikut Chat.",
    "Responjoin":"Thanks For Invite Me",
    "Responleave":"Thanks For Invite Me\nGoodbye, See You Next Time",
    "Respontag":"Jangan Tag, Aku Lagi Sibuk.",
    "comment":"Auto Like & Comment : NIAR TEAM BOT",
    "message":"Terimakasih, Sudah Add Saya 😎.",
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
dzProfile = cl.getProfile()
myProfile["displayName"] = dzProfile.displayName
myProfile["statusMessage"] = dzProfile.statusMessage
myProfile["pictureStatus"] = dzProfile.pictureStatus

    
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def logError(text):
    cl.log("[ NIAR TEAM BOT ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Bandung")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("errorLog.txt","a") as error:
        error.write("\n[{}] {}".format(str(time), text))

def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost

def sendTextTemplate(to, text):
    data = {
            "type": "flex",
            "altText": "Mengirim Pesan",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "md",
                "margin": "none",
                "color": "#C0C0C0",
                "wrap": True,
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)
        
def sendTextTemplate1(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} Mengirim Pesan".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#C0C0C0"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00FF00"
    },
    "header": {
      "backgroundColor": "#00FF00"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://media.giphy.com/media/2rACoMVCPOdxYzpLvO/giphy.gif",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~noviansyah39"
        },        
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "N̸I̸A̸R̸ T̸E̸A̸M̸ B̸O̸T̸",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#00000",
        "align": "center"
      }
    ]
  }
}
}
    cl.postTemplate(to, data)

def sendTextTemplate2(to, text):
    data = {
            "type": "flex",
            "altText": "Broadcast",
            "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "sm",
            "weight": "bold",
            "wrap": True,
            "color": "#C0C0C0",
            "align": "center"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00FF00"
    },
    "header": {
      "backgroundColor": "#00FF00"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~noviansyah39"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "BROADCAST",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "align": "center"
      }
    ]
  }
}
}
    cl.postTemplate(to, data)

def sendTextTemplate3(to, text):
    data = {
            "type": "flex",
            "altText": "Mengirim Pesan",
            "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "sm",
            "weight": "bold",
            "wrap": True,
            "color": "#C0C0C0"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00FF00"
    },
    "header": {
      "backgroundColor": "#00FF00"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~noviansyah39"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "N̸I̸A̸R̸ T̸E̸A̸M̸ B̸O̸T̸",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "align": "center"
      }
    ]
  }
}
}
    cl.postTemplate(to, data)

def sendTextTemplate4(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} Mengirim Pesan".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#C0C0C0"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00FF00"
    },
    "header": {
      "backgroundColor": "#00FF00"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://media.giphy.com/media/2rACoMVCPOdxYzpLvO/giphy.gif",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~noviansyah39"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text",
        "text": "ORDER",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "action": {
          "type": "uri",
          "uri": "line://app/1602687308-GXq4Vvk9/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "N̸I̸A̸R̸ T̸E̸A̸M̸ B̸O̸T̸",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "align": "center"
      }
    ]
  }
}
}
    cl.postTemplate(to, data)

def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
                          "type": "template",
                          "altText": "{} Sent a sticker".format(cl.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/~noviansyah39"
           }                                                
 }
]
                          }
                      }
    cl.postTemplate(to, data)
    
def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))
        
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
            
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def downloadImageWithURL (mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        client.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = client.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)
    
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            client.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        sendTextTemplate(tmp, "📟 Bot Kembali Aktif...")
                    except Exception as error:
                        logError(error)
                        
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
                        
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))

def changeProfileVideo(to):
    if settings['changeProfileVideo']['picture'] == None:
        return cl.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changeProfileVideo']['video'] == None:
        return cl.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changeProfileVideo']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendMessage(to, "Gagal update profile")
        path_p = settings['changeProfileVideo']['picture']
        settings['changeProfileVideo']['status'] = False
        cl.updateProfilePicture(path_p, 'vp')

def cloneProfile(mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)

def restoreProfile():
    profile = cl.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        cl.updateProfileAttribute(8, profile.pictureStatus)
        cl.updateProfile(profile)
    else:
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    cl.updateProfileCoverById(coverId)
    
def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)

def backupProfile():
    profile = cl.getContact(mid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = cl.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention「{}」\n\n•".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "•"
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error)) 

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Sider User「{}」\nHello ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += "welcome"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
      #  client.sendMessage(to, textx)
    except Exception as error:
        cl.sendMessage(to)
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += "babay"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
        #client.sendMessage(to, textx)
    except Exception as error:
        cl.sendMessage(to)
        
def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"➳ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n➳ Group : "+str(len(gid))+"\n➳ Teman : "+str(len(teman))+"\n➳ Expired : In "+hari+"\n➳ Version : 『PY3 - 2019』 \n➳ Tanggal : "+datetime.strftime(timeNow,'%d-%m-%Y')+"\n➳ Runtime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(msg.to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain['keyCommand']):
        cmd = pesan.replace(Setmain['keyCommand'],"")
    else:
        cmd = "command"
    return cmd

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
                                
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate(op.param1,wait["Responleave"])
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate(op.param1,wait["Responjoin"])

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate(op.param1,wait["Responjoin"])
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate(op.param1,wait["Responjoin"])

        if op.type == 17:
            if op.param1 in welcome:
                ginfo = cl.getGroup(op.param1)
                welcomeMembers(op.param1, [op.param2])
                contact = cl.getContact(op.param2)
                data = {
                        "type": "flex",
                        "altText": "Mengirim Pesan",
                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "flex": 2,
            "text": "{}".format(cl.getContact(op.param2).displayName),
            "size": "md",
            "wrap": True,
            "weight": "bold",
            "gravity": "center",
            "color": "#000000"
          },
          {
            "type": "separator",
            "color": "#000000"
          },
          {
            "type": "text",
            "text": "WELCOME",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#C0C0C0",
            "align": "center"
          },
          {
            "type": "text",
            "text": "Selamat Datang & Selamat Bergabung Kawan.\nJangan Lupa Jalan2 Ke Note Ya Kak, Dan Tingggalkan Jejak Dengan Like Note Nya.\nTerimakasih...",
            "size": "md",
            "weight": "bold",
            "color": "#C0C0C0",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00FF00"
    }
  },
  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
    "size": "full",
    "margin": "xxl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~noviansyah39"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text",
        "text": "ORDER",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "action": {
          "type": "uri",
          "uri": "line://app/1603968955-ORWb9RdY/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  }
}
}
                cl.postTemplate(op.param1, data)
                sendStickerTemplate(op.param1, "https://i.gifer.com/XfQ8.gif")

        if op.type == 15:
            if op.param1 in welcome:
                ginfo = cl.getGroup(op.param1)
                leaveMembers(op.param1, [op.param2])
                contact = cl.getContact(op.param2).picturePath
                data = {
                        "type": "flex",
                        "altText": "Mengirim Pesan",
                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "flex": 2,
            "text": "{}".format(cl.getContact(op.param2).displayName),
            "size": "md",
            "wrap": True,
            "weight": "bold",
            "gravity": "center",
            "color": "#000000"
          },
          {
            "type": "separator",
            "color": "#000000"
          },
          {
            "type": "text",
            "text": "GOOD BYE",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#C0C0C0",
            "align": "center"
          },
          {
            "type": "text",
            "text": "Selamat Jalan, Semoga Bahagia Diluar Sana.",
            "size": "md",
            "weight": "bold",
            "color": "#C0C0C0",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00FF00"
    }
  },
  
  "hero": {
    "aspectRatio": "20:13",
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
    "size": "full",
    "margin": "xxl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~noviansyah39"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text",
        "text": "ORDER",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "action": {
          "type": "uri",
          "uri": "line://app/1603968955-ORWb9RdY/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  }
}
}
                cl.postTemplate(op.param1, data)
                sendStickerTemplate(op.param1, "https://thumbs.gfycat.com/UnnaturalBelatedAmericansaddlebred-max-1mb.gif")

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])
  
        if op.type == 17:
            if op.param2 in wait["blacklist"] == True:
                cl.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass                                                          
                return

        if op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                terminal = command(text)
                for terminal in terminal.split(" & "):
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != cl.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:
                            if to in offbot:
                                return
                        elif msg.contentType == 16:
                            if settings["checkPost"] == True:
                                try:
                                    ret_ = "Details Post"
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        contact = cl.getContact(sender)
                                        auth = "\nPenulis : {}".format(str(contact.displayName))
                                    else:
                                        auth = "\nPenulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                    purl = "\nURL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                    ret_ += auth
                                    ret_ += purl
                                    if "mediaOid" in msg.contentMetadata:
                                        object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                        if msg.contentMetadata["mediaType"] == "V":
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                                murl = "\nMedia URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                                murl = "\nMedia URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                            ret_ += murl
                                        else:
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        ret_ += ourl
                                    if "stickerId" in msg.contentMetadata:
                                        stck = "\nStiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                        ret_ += stck
                                    if "text" in msg.contentMetadata:
                                        text = "\nTulisan :\n{}".format(str(msg.contentMetadata["text"]))
                                        ret_ += text
                                    ret_ += "\nFinish"
                                    cl.sendMessage(to, str(ret_))
                                except:
                                    sendTextTemplate(to, "❂➣ Post Tidak Valid... !!!")
                            if msg.toType in (2,1,0):
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                adw = cl.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                                adws = cl.createComment(purl[0], purl[1], settings["commentPost"])
                                sendTextTemplate(to, "❂➣ Done Like & Comment Bos...")
            except Exception as error:
                logError(error)

        if op.type in [25, 26]:           
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != mid: to = sender
                else: to = receiver
                if receiver in temp_flood:
                    if temp_flood[receiver]["expire"] == True:
                        if cmd == "open" and sender == mid:
                            temp_flood[receiver]["expire"] = False
                            temp_flood[receiver]["time"] = time.time()
                            sendTextTemplate(to, "📟 Bot Kembali Aktif...")
                        return
                    elif time.time() - temp_flood[receiver]["time"] <= 5:
                        temp_flood[receiver]["flood"] += 1
                        if temp_flood[receiver]["flood"] >= 20:
                            temp_flood[receiver]["flood"] = 0
                            temp_flood[receiver]["expire"] = True
                            ret_ = "🚨 Spam Terdeteksi... !!!".format(setKey)
                            ret_ = "📟 Bot Akan Off Sementara.".format(setKey)
                            sendTextTemplate(to, str(ret_))
                    else:
                         temp_flood[receiver]["flood"] = 0
                         temp_flood[receiver]["time"] = time.time()
                else:
                    temp_flood[receiver] = {
    	                "time": time.time(),
    	                "flood": 0,
    	                "expire": False
                    }

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                cl.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 55:            
            try:
                if op.param1 in read["readPoint"]:
                    if op.param2 in read["readMember"][op.param1]:
                        pass
                    else:
                        read["readMember"][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    
        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        data = {
                                "type": "flex",
                                "altText": "Sider",
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "Terciduk",
            "size": "xl",
            "weight": "bold",
            "wrap": True,
            "color": "#C0C0C0",
            "align": "center"
          },
          {
            "type": "text",
            "text": "Iya Dech, Aku Ngaku...\nKalau Aku Ini Tukang Ngintip.",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#C0C0C0"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00FF00"
    },
    "header": {
      "backgroundColor": "#00FF00"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
    "size": "full",
    "margin": "xxl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~noviansyah39"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(cl.getContact(op.param2).displayName),
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "align": "center"
      }
    ]
  }
}
}
                        cl.postTemplate(op.param1, data)

            if msg.contentType == 16:
                       url = msg.contentMetadata["postEndUrl"]
                       cl.like(url[25:58], url[66:], likeType=1001)                       
                       cl.comment(url[25:58], url[66:], wait["comment"])
                                                        
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          cl.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              cl.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              try:
                                  cl.kickoutFromGroup(msg.to, [msg._from])
                              except:
                              	pass
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           sendTextTemplate(to, wait["Respontag"])
                           break   
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(to, "Cek ID Sticker\n\nSTKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(to, "Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(to, "STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(to, "Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(to, image)

               if msg.contentType == 0:
                  if settings["autoRead"] == True:
                      cl.sendChatChecked(to, msg_id)
                      print ("Read")
                  if text is None:
                      return
                  else:
                         for sticker in stickers:
                          if msg._from in mid:
                            if text.lower() == sticker:
                               sid = stickers[text.lower()]["STKID"]
                               spkg = stickers[text.lower()]["STKPKGID"]
                               cl.sendSticker(to, spkg, sid)
                         for image in images:
                          if msg._from in mid:
                            if text.lower() == image:
                               cl.sendImage(to, images[image])
                         for audio in audios:
                          if msg._from in mid:
                            if text.lower() == audio:
                               cl.sendAudio(to, audios[audio])
                         for video in videos:
                          if msg._from in mid:
                            if text.lower() == video:
                               cl.sendVideo(to, videos[video])
         
               if msg.contentType == 1:
                 if msg._from in owner:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            sendTextTemplate(to, "Succes Add Picture")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(to, path)
                     sendTextTemplate(to, "Succes Change Pict Group")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if mid in Setmain["RAfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][mid]
                            cl.updateProfilePicture(path)
                            sendTextTemplate(to, "Foto berhasil dirubah")
#=================================================================================#
               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)                                                                             
                        if cmd == "self on":
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["selfbot"] = True
                                sendTextTemplate(msg.to, "Self Telah Diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in owner or msg._from in admin:
                                wait["selfbot"] = False
                                sendTextTemplate(msg.to, "Self Off Sementara Waktu")                                                                            

                        elif cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate4(msg.to, "【♻】Help\n"
"【♻】Key1\n"
"【♻】Key2\n"
"【♻】Key3\n"
"【♻】Key4\n"
"【♻】About\n"
"【♻】Runtime\n"
"【♻】Sticker\n"
"【♻】Setting\n"
"【♻】Broadcast:「Text」\n")

                        elif cmd == "key1":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate4(msg.to, "【♻】Self「on / off」\n"
"【♻】Me\n"
"【♻】Aku\n"
"【♻】Tag / Woy\n"
"【♻】Kick「@」\n"
"【♻】Invite「@」\n"
"【♻】Cancelall\n"
"【♻】Sp / Speed\n"
"【♻】Pamit\n"
"【♻】Curl\n"
"【♻】Ourl\n"
"【♻】Restart\n"
"【♻】Refresh\n")

                        elif cmd == "key2":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate4(msg.to, "【♻】Music「Judul Lagu」\n"
"【♻】Ytmp4:「Judul Lagu」\n"
"【♻】Ginfo\n"
"【♻】Grouplist\n"
"【♻】Updategroup\n"
"【♻】Updatefoto\n"
"【♻】Get id 「@」\n"
"【♻】Info「@」\n"
"【♻】Clone「@」\n"
"【♻】Lc「@」\n"
"【♻】Blc / Banlist\n"
"【♻】Clearban\n"
"【♻】Refresh\n")

                        elif cmd == "key3":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate4(msg.to, "【♻】Respon「on / off」\n"
"【♻】Sider「on / off」\n"
"【♻】Welcome「on / off」\n"
"【♻】Autojoin「on / off」\n"
"【♻】Autoleave「on / off」\n"
"【♻】Autoadd「on / off」\n"
"【♻】Autoblock「on / off」\n"
"【♻】Checkpost「on / off」\n"
"【♻】Contact「on / off」\n"
"【♻】Sticker「on / off」\n"
"【♻】Refresh\n")

                        elif cmd == "key4":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate4(msg.to, "【♻】Set pesan:「Text」\n"
"【♻】Set welcome:「Text」\n"
"【♻】Set respon:「Text」\n"
"【♻】Set sider:「Text」\n"
"【♻】Cek pesan\n"
"【♻】Cek welcome\n"
"【♻】Cek respon\n"
"【♻】Cek sider\n"
"【♻】Cek akun\n"
"【♻】Refresh\n")

                        elif cmd == "setting":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "SETTING\n\n"
                                if msg.to in welcome: md+="【✔】Welcome\n"
                                else: md+="【🚫】Welcome\n"
                                if wait["autoJoin"] == True: md+="【✔】Autojoin\n"
                                else: md+="【🚫】Autojoin\n"
                                if wait["autoLeave"] == True: md+="【✔】Autoleave\n"
                                else: md+="【🚫】Autoleave\n"
                                if wait["autoAdd"] == True: md+="【✔】Autoadd\n"
                                else: md+="【🚫】Autoadd\n"
                                if wait["sticker"] == True: md+="【✔】Sticker\n"
                                else: md+="【🚫】Sticker\n"                                
                                if wait["contact"] == True: md+="【✔】Contact\n"
                                else: md+="【🚫】Contact\n"                                
                                if wait["detectMention"] == True: md+="【✔】Respon\n"
                                else: md+="【🚫】Respon\n"
                                if settings["unsendMessage"] == True: md+="【✔】Unsend\n"
                                else: md+="【🚫】Unsend\n"                                                                                                                                                                                                
                                sendTextTemplate3(msg.to, md+"\nDate  : "+ datetime.strftime(timeNow,'%d-%m-%Y')+"\nTime : "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                      
                        elif cmd == "about":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               sendTextTemplate3(msg.to, "【♻】Type : Selfbot\n"
"【♻】Version : PY3 - 2019\n"
"【♻】Library : linepy\n"
"【♻】Model : Template\n\n"
"Date  : "+ datetime.strftime(timeNow,'%d-%m-%Y')+"\nTime : "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                                                                                                                                                                             
                        elif cmd == "aku" or text.lower() == 'aku':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getContact(sender)
                               cl.sendMessage(msg.to,"╭❂➣━━━━━━━━━━━━━➣\n""┃    "+str(cl.getProfile().displayName)+"\n╰❂➣━━━━━━━━━━━━━➣")
                               cl.sendMessage(msg.to, None,contentMetadata={'mid': sender}, contentType=13)
                               contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+contact.pictureStatus, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': contact.statusMessage, 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': contact.displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://line.me.naver.jp/line/p/",'MSG_SENDER_NAME':  contact.displayName,}
                               cl.sendMessage(msg.to, contact.displayName, contentMetadata, 19)
                                           
                        elif ("Get id " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               sendTextTemplate(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               
                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               sendTextTemplate(msg.to, "Nama : "+str(mi.displayName)+"\nMid : " +key1+"\nStatus Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))
                                   
                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   sendTextTemplate2(group,"〘 ASSALAMUALAIKUM 〙\n\n" + str(pesan))
                        
                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "⏳Reload...")
                               sendTextTemplate(msg.to, "Silahkan Gunakan Seperti Semula")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                                                 
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Active " +waktu(eltime)
                               sendTextTemplate(to,bot)
                               
                        elif cmd == "sticker":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate3(msg.to, "【♻】Assalamualaikum\n"
"【♻】Sedih\n"
"【♻】Jomblo\n"
"【♻】Sue\n"
"【♻】Terimakasih\n"
"【♻】Mbuh/Mboh\n"
"【♻】Naik\n"
"【♻】Bye\n"
"【♻】Sepi\n"
"【♻】Kabur\n")
            
                        elif cmd == "ginfo":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak Ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                sendTextTemplate(to, "Group Info\n\nNama Group : {}".format(G.name)+ "\nID Group : {}".format(G.id)+ "\nPembuat : {}".format(G.creator.displayName)+ "\nWaktu Dibuat : {}".format(str(timeCreated))+ "\nJumlah Member : {}".format(str(len(G.members)))+ "\nJumlah Pending : {}".format(gPending)+ "\nGroup Qr : {}".format(gQr)+ "\nGroup Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                sendTextTemplate(to, str(e))                                                                 
                                
                        elif cmd == "me":
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                status = cl.getContact(sender)                               	
                                data = {
                                        "type": "flex",
                                        "altText": "Mengirim Pesan",
                                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "Status :",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#C0C0C0"
          },
          {
            "type": "text",
            "text": "{}".format(status.statusMessage),
            "align": "center",
            "size": "sm",
            "weight": "bold",
            "color": "#C0C0C0",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00FF00"
    },
    "header": {
      "backgroundColor": "#00FF00"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~noviansyah39"
        },
        "align": "center"
      }
    ]
  },
  "hero": {
    "aspectMode": "cover",
    "aspectRatio": "20:13",
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
    "size": "full",
    "align": "center",
  },
  "header": {
    "type": "box",   
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(status.displayName),
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "align": "center"
      }
    ]
  }
}
}
                                cl.postTemplate(to, data)
                                                                                           
                        elif "jomblo" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} Mengirim Sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://4.bp.blogspot.com/-f1Ac9hha1NA/WE_QkvJGBEI/AAAAAAAFMuA/xNeS9_M2O0M3t2cv6YFjHSLlD8TcAW6GwCLcB/s1600/AW293929_02.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~noviansyah39"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif "sue" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} Mengirim Sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://3.bp.blogspot.com/-CXej0VEJkps/WDv1XSwipPI/AAAAAAALlNU/UjrTOos8KF86vkw05SE25bUkAQc86b2pwCLcB/s1600/AS001630_08.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~noviansyah39"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
  
                        elif "terimakasih" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} Mengirim Sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://3.bp.blogspot.com/-DcGGuaPMWUk/WVRjBYIJa5I/AAAAAAAIo5k/YyEwYgikZa8p1d05X04bB3rhqCMgL52ewCLcBGAs/s1600/AS002777_01.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~noviansyah39"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
     
                        elif "mbuh" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} Mengirim Sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://mastergolflivestream.com/images/clipart-monkey-gif-animation-8.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~noviansyah39"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
   
                        elif "mboh" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} Mengirim Sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://mastergolflivestream.com/images/clipart-monkey-gif-animation-8.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~noviansyah39"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
     
                        elif "naik" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} Mengirim Sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://4.bp.blogspot.com/-H6CCaBKZx80/WymRq9o_HMI/AAAAAAAgatE/TGJNvRBure4TBDdqFelwB0r4UE0FkGg7wCLcBGAs/s1600/AW1238435_06.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~noviansyah39"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
     
                        elif "bye" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} Mengirim Sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://2.bp.blogspot.com/-JYruBBpWAT8/WN5gF4SZvzI/AAAAAAAOTwA/cQm1k193EtY0Q5Bb7RpsX8px2mfaxsSMACLcB/s1600/AW400539_23.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~noviansyah39"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif "kabur" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} Mengirim Sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://3.bp.blogspot.com/-cpA0qRAqi1k/WymK7QB3O-I/AAAAAAAgZ6I/hGoxo__H4yMEWk-K7WgShHTD__qY6Uf-ACLcBGAs/s1600/AW1238279_09.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~noviansyah39"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                        
                        elif "assalamualaikum" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} Mengirim Sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://thumbs.gfycat.com/FirstPeriodicChimpanzee-size_restricted.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~noviansyah39"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif "sepi" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} Mengirim Sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://4.bp.blogspot.com/-nJ4iMqsxTQc/WwJ97etgoiI/AAAAAAAIoGM/_mG-H0OhIPMLPdJ85ApFDB9Nzxqr_74IwCLcBGAs/s1600/AW1084508_09.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~noviansyah39"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif cmd == "grouplist":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               sendTextTemplate(msg.to,"GROUP LIST\n\n"+ma+"\nTotal"+str(len(gid))+" Groups")

                        elif cmd == "curl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   sendTextTemplate(msg.to, "Url Closed")

                        elif cmd == "ourl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl Group : http://line.me/R/ti/g/"+gurl)

                        elif cmd == "updategroup":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                sendTextTemplate(msg.to, "Send Picture...")                     
                                                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["RAfoto"][mid] = True
                                sendTextTemplate(msg.to, "Send picture")

                        elif cmd == "tag" or text.lower() == 'woy':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1,nm2,nm3,nm4,nm5,nm6,nm7,nm8,nm9,nm10,nm11,nm12, jml = [], [], [], [],[], [], [], [], [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                               if jml > 160 and jml < 180:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for o in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)                                   
                                   for p in range (160, len(nama)-1):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                               if jml > 180 and jml < 200:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for o in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)                                   
                                   for o in range (160, 179):
                                       nm8 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for p in range (180, len(nama)-1):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                               if jml > 200 and jml < 220:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for o in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)                                   
                                   for o in range (160, 179):
                                       nm8 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for o in range (180, 199):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for p in range (200, len(nama)-1):
                                       nm10 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                               if jml > 220 and jml < 240:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for o in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)                                   
                                   for o in range (160, 179):
                                       nm8 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for o in range (180, 199):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for o in range (200, 219):
                                       nm10 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                                   for p in range (220, len(nama)-1):
                                       nm10 += [nama[t]]
                                   mentionMembers(msg.to, nm12)
                               if jml > 240 and jml < 260:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for o in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)                                   
                                   for o in range (160, 179):
                                       nm8 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for o in range (180, 199):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for o in range (200, 219):
                                       nm10 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                                   for o in range (220, 239):
                                       nm10 += [nama[t]]
                                   mentionMembers(msg.to, nm12)
                                   for p in range (240, len(nama)-1):
                                       nm10 += [nama[u]]
                                   mentionMembers(msg.to, nm13) 
                                                                                                       
                        elif cmd == "pamit":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(to)
                                sendTextTemplate(msg.to, "Goodbye Friends "+str(G.name))
                                sendTextTemplate(msg.to, "Assalamualaikum Warahmatullahi Wabarakatuh ")
                                cl.leaveGroup(to)
                                                                                                                                                               
                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:                              
                               start = time.time()
                               time.sleep(0.001)
                               get_profile_time_start = time.time()
                               get_profile = cl.getProfile()
                               get_profile_time = time.time() - get_profile_time_start
                               sendTextTemplate(msg.to, "Speed Progress...")
                               sendTextTemplate(msg.to, "Time :\n「%.8f」Seconds" % (get_profile_time/3))
                                                                                                                                                                                                                                                                          
                        elif cmd == "sider on" or cmd == "cctv on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendTextTemplate(to, "『CEK SIDER ON』\n\n📆 Tanggal : "+ datetime.strftime(timeNow,'%d-%m-%Y')+"\n⏰ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off" or cmd == "cctv off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendTextTemplate(to, "『CEK SIDER OFF』\n\n📆 Tanggal : "+ datetime.strftime(timeNow,'%d-%m-%Y')+"\n⏰ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  sendTextTemplate(to, "『CEK SIDER OFF』\n\n📆 Tanggal : "+ datetime.strftime(timeNow,'%d-%m-%Y')+"\n⏰ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif 'lc ' in text.lower():
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = cl.getContact(u).mid
                                    s = cl.getContact(u).displayName
                                    hasil = cl.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        cl.likePost(str(sender), str(result), likeType=random.choice(typel))
                                        cl.createComment(str(sender), str(result), 'Auto Like & Comment : NIAR TEAM BOT')
                                    sendTextTemplate(to, 'Done Like + Comment '+str(len(st))+' Post From' + str(s))
                                except Exception as e:
                                    cl.sendMessage(receiver, str(e))
                                                                                                                                                  
                        elif cmd.startswith("ytmp4: "):
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\nAuthor : ' + str(vid.author)
                                    durasi = '\nDuration : ' + str(vid.duration)
                                    suka = '\nLikes : ' + str(vid.likes)
                                    rating = '\nRating : ' + str(vid.rating)
                                    deskripsi = '\nDeskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                sendTextTemplate(to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                sendTextTemplate(to,str(e))
                                
                        elif cmd.startswith("clone "):
                           if msg._from in admin:
                             if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    cl.cloneContactProfile(contact)
                                    ryan = cl.getContact(contact)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan =  "「 Clone Profile 」\nTarget Nya "
                                    ret_ = "Berhasil Clone Profile Target"
                                    ry = str(ryan.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except:
                                    sendTextTemplate(msg.to, "Gagal Clone Profile")       

                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg Sudah Aktif"
                                  else:
                                       welcome.append(to)
                                       ginfo = cl.getGroup(to)
                                       msgs = "Welcome Msg Diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(to)
                                         ginfo = cl.getGroup(to)
                                         msgs = "Welcome Msg Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg Sudah Tidak Aktif"
                                    sendTextTemplate(msg.to, "「Dinonaktifkan」\n" + msgs)     

                        elif ("Kick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           cl.kickoutFromGroup(msg.to,[target])
                                       except:
                                           pass
                                                                                             
                        elif "Invite " in msg.text:
                            if msg._from in admin:                                                                                                                                       
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]                                                                                                                                
                               targets = []
                               for x in key["MENTIONEES"]:                                                                                                                                  
                                   targets.append(x["M"])
                               for target in targets:                                                                                                                                       
                                   try:
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                   except:
                                       pass
           
                        elif cmd == "cancelall" and sender == mid:
                            if msg.toType == 2:
                                group = cl.getGroup(to)
                                if group.invitee is None or group.invitee == []:
                                    sendTextTemplate(to, "🚫 No Member Must Be Canceled")
                                else:
                                    invitee = [contact.mid for contact in group.invitee]
                                    for inv in invitee:
                                        cl.cancelGroupInvitation(to, [inv])
                                        time.sleep(0.001)
                                    sendTextTemplate(to, "✔Managed To Clean Up\n「{}」Pending Member".format(str(len(invitee))))

                        elif cmd == "autojoin on":
                            if msg._from in owner:
                                settings["autoJoin"] = True
                                sendTextTemplate(msg.to, "Berhasil mengaktifkan auto join")
                        elif cmd == "autojoin off":
                            if msg._from in owner:	
                                settings["autoJoin"] = False
                                sendTextTemplate(msg.to, "Berhasil menonaktifkan auto join")
                        elif cmd == "autoblock on":
                           if msg._from in owner:
                                settings["autoBlock"] = True
                                sendTextTemplate(msg.to, "Berhasil mengaktifkan auto Block")
                        elif cmd == "autoblock off":    
                            if msg._from in owner: 	
                                settings["autoBlock"] = False
                                sendTextTemplate(msg.to, "Berhasil menonaktifkan auto Block")                        
                        elif cmd == "checkpost on":
                           if msg._from in owner:
                                 settings["checkPost"] = True
                                 sendTextTemplate(msg.to, "Berhasil mengaktifkan check details post")
                        elif cmd == "checkpost off":
                           if msg._from in owner:
                                settings["checkPost"] = False
                                sendTextTemplate(msg.to, "Berhasil menonaktifkan check details post")                        
                        elif cmd == "unsend on":
                       	 if msg._from in owner:
                                 settings["unsendMessage"] = True
                                 sendTextTemplate(msg.to, "Berhasil mengaktifkan unsend message")
                        elif cmd == "unsend off":
                            if msg._from in owner:
                                 settings["unsendMessage"] = False
                                 sendTextTemplate(msg.to, "Berhasil menonaktifkan unsend message")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                sendTextTemplate(msg.to,"Clean...")
                                sendTextTemplate(msg.to,"Refresh Done 💯")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = True
                                sendTextTemplate(msg.to,"Deteksi Contact Diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = False
                                sendTextTemplate(msg.to,"Deteksi Contact Dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = True
                                sendTextTemplate(msg.to,"Auto Respon Diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = False
                                sendTextTemplate(msg.to,"Auto Respon Dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoJoin"] = True
                                sendTextTemplate(msg.to,"Autojoin Diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoJoin"] = False
                                sendTextTemplate(msg.to,"Autojoin Dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                                wait["autoLeave"] = True
                                sendTextTemplate(msg.to,"Autoleave Diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoLeave"] = False
                                sendTextTemplate(msg.to,"Autoleave Dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = True
                                sendTextTemplate(msg.to,"Auto Add Diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = False
                                sendTextTemplate(msg.to,"Auto Add Dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = True
                                sendTextTemplate(msg.to,"Deteksi Sticker Diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = False
                                sendTextTemplate(msg.to,"Deteksi Sticker Dinonaktifkan")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                              if wait["blacklist"] == {}:
                                sendTextTemplate(to,"Nothing Blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"Blacklist\n\n"+ma+"\n %s User" %(str(len(wait["blacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["blacklist"] == {}:
                                    sendTextTemplate(msg.to,"Nothing Blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "%i" % len(ragets)
                              sendTextTemplate(msg.to, "Succes Clear All Blacklist")

                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  sendTextTemplate(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  sendTextTemplate(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  sendTextTemplate(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  sendTextTemplate(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")
                               
                        elif cmd == "cek akun":
                            if msg._from in admin or msg._from in owner:
                               try:cl.inviteIntoGroup(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               sendTextTemplate(msg.to, "Status :\n\n🔥Kick : {}\n🔥Invite : {}".format(sil1,sil))
                      

    except Exception as error:
        print (error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                #NIAR TEAM BOT : Noviansyah|ID Line : noviansyah39
                # Don't remove this line, if you wan't get error soon!
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)