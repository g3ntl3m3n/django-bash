rom django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json,requests
from subprocess import Popen, PIPE, STDOUT



def create_directory():

        komut = ["bash","easyaslinux/scripts/file_manipulater.sh","create" ]
        try:
                islem = Popen(komut, stdout=PIPE, stderr=STDOUT)
                output = islem.stdout.read()
                status = islem.poll()
                if (status==0):
                        return {"status": "Basarili", "output":str(output)}
                else:
                        return {"status": "Hata", "output":str(output)}
        except Exception as e:
                return {"status": "Hata", "output":str(e)}


def delete_directory():

        komut = ["bash","easyaslinux/scripts/file_manipulater.sh","delete" ]
        try:
               islem = Popen(komut, stdout=PIPE, stderr=STDOUT)
                output = islem.stdout.read()
                status = islem.poll()
                if (status==0):
                        return {"status": "Basarili", "output":str(output)}
                else:
                        return {"status": "Hata", "output":str(output)}
        except Exception as e:
                return {"status": "Hata", "output":str(e)}



@csrf_exempt
def file_man(request):

        if request.method == 'POST':
                request_data=json.loads(request.body)

                if request_data["action"] == "create":
                        data = create_directory()
                elif request_data["action"] == "delete":
                        data  =delete_directory()
                else:
                        data = {"status": "tanimlanmamis", "output":"tanimlanmamis"}

                response = HttpResponse(json.dumps(data) , content_type='application/json', status=200)
                return response
