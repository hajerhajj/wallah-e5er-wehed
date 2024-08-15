# accounts/views.py
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from DashApp.models import OrAdmin
import os
from django.conf import settings
from .models import Int, Tn1EPG, Tn1MME,Tn2MME,SoMME , SOEPG, TN2VEPG, Tn1APN, Tn2APN, SOAPN, Tn2VEPGAPN,Tn2EPG
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _


@login_required
def HomePage(request):
    context = {
        'tn1_data': Tn1MME.objects.all().order_by('-date'),
        'tn2_data': Tn2MME.objects.all().order_by('-date'),
        'sousse_data': SoMME.objects.all().order_by('-date'),
        'tn1global_data': Tn1MME.objects.all().order_by('-date'),
        'tn2global_data': Tn2MME.objects.all().order_by('-date'),
        'sousseglobal_data': SoMME.objects.all().order_by('-date'),
        'int_data': Int.objects.all().order_by('-date'),
        'tn1epg_data': Tn1EPG.objects.all().order_by('-date'),
        'tn2epg_data': Tn2EPG.objects.all().order_by('-date'),
        'tn2vepg_data': TN2VEPG.objects.all().order_by('-date'),
        'soepg_data': SOEPG.objects.all().order_by('-date'),
    }

    response = render(request, 'index.html', context)
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    
    return response

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Your password was successfully updated!'))
            return redirect('change_password')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })       
    


from django.contrib import messages

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if OrAdmin.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered!")
        else:
            or_admin = OrAdmin(username=uname, email=email)
            or_admin.set_password(password)  # Utiliser set_password pour sécuriser le mot de passe
            or_admin.save()
            return redirect('login')

    return render(request, 'signup.html', {})

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = OrAdmin.objects.get(username=username)
            if user.check_password(password):
                login(request, user)
                return redirect('index')  # Assurez-vous que 'index' est bien défini
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect!")
        except OrAdmin.DoesNotExist:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect!")
    
    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')



def readfiletn1_function():
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'resultmmetn1.txt')
    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip():
                    data = line.strip().split('|')
                    if len(data) >= 8:
                        try:
                            date_str = data[0].strip()
                            attach2g3g = float(data[1].strip())
                            attach4g = float(data[2].strip())
                            pdpact2g3g = float(data[3].strip())
                            attach3g = float(data[4].strip())
                            sau2g3g = int(float(data[5].strip()))
                            sau4g = int(float(data[6].strip()))
                            pdp = int(float(data[7].strip()))
                            bearer = int(float(data[8].strip()))
                            pdpactnbr2g = int(float(data[9].strip()))
                            pdpactnbr3g = int(float(data[10].strip()))

                            mm_instance, created = Tn1MME.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'attach2g3g': attach2g3g,
                                    'attach4g': attach4g,
                                    'pdpact2g3g': pdpact2g3g,
                                    'attach3g': attach3g,
                                    'sau2g3g': sau2g3g,
                                    'sau4g': sau4g,
                                    'pdp': pdp,
                                    'bearer': bearer,
                                    'pdpactnbr2g': pdpactnbr2g,
                                    'pdpactnbr3g': pdpactnbr3g,
                                }
                            )
                        except (ValueError, IndexError) as e:
                            continue

    else:
        print(f"Fichier non trouvé dans le répertoire spécifié.")

def readfiletn1(request):
    readfiletn1_function()
    return HttpResponse("Données du fichier importées dans la base PostgreSQL.")   
    
    
def readfiletn2_function():
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'resultmmetn2.txt')
    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip():  # Ignore empty lines
                    data = line.strip().split('|')
                    if len(data) >= 8: 
                        try:
                            date_str = data[0].strip()
                            attach2g3g = float(data[1].strip())
                            attach4g = float(data[2].strip())
                            pdpact2g3g = float(data[3].strip())
                            attach3g = float(data[4].strip())
                            sau2g3g = int(float(data[5].strip()))
                            sau4g = int(float(data[6].strip()))
                            pdp = int(float(data[7].strip()))
                            bearer = int(float(data[8].strip()))
                            pdpactnbr2g = int(float(data[9].strip()))
                            pdpactnbr3g = int(float(data[10].strip()))

                            # Create or update instance of Tn1MME model
                            mm_instance, created = Tn2MME.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'attach2g3g': attach2g3g,
                                    'attach4g': attach4g,
                                    'pdpact2g3g': pdpact2g3g,
                                    'attach3g': attach3g,
                                    'sau2g3g': sau2g3g,
                                    'sau4g': sau4g,
                                    'pdp': pdp,
                                    'bearer': bearer,
                                    'pdpactnbr2g': pdpactnbr2g,
                                    'pdpactnbr3g': pdpactnbr3g,
                                }
                            )

                        except (ValueError, IndexError) as e:
                            continue

    else:
        print(f"Fichier non trouvé dans le répertoire spécifié.")


def readfiletn2(request):
    readfiletn2_function()
    return HttpResponse("Données du fichier importées dans la base PostgreSQL.")  
    
    
def readfileso_function():
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'resultmmeso.txt')
    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip():  # Ignore empty lines
                    data = line.strip().split('|')
                    if len(data) >= 8: 
                        try:
                            date_str = data[0].strip()
                            attach2g3g = float(data[1].strip())
                            attach4g = float(data[2].strip())
                            pdpact2g3g = float(data[3].strip())
                            attach3g = float(data[4].strip())
                            sau2g3g = int(float(data[5].strip()))
                            sau4g = int(float(data[6].strip()))
                            pdp = int(float(data[7].strip()))
                            bearer = int(float(data[8].strip()))
                            pdpactnbr2g = int(float(data[9].strip()))
                            pdpactnbr3g = int(float(data[10].strip()))

                            mm_instance, created = SoMME.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'attach2g3g': attach2g3g,
                                    'attach4g': attach4g,
                                    'pdpact2g3g': pdpact2g3g,
                                    'attach3g': attach3g,
                                    'sau2g3g': sau2g3g,
                                    'sau4g': sau4g,
                                    'pdp': pdp,
                                    'bearer': bearer,
                                    'pdpactnbr2g': pdpactnbr2g,
                                    'pdpactnbr3g': pdpactnbr3g,
                                }
                            )

                        except (ValueError, IndexError) as e:
                            continue

    else:
        print(f"Fichier non trouvé dans le répertoire spécifié.")


def readfileso(request):
    readfileso_function()
    return HttpResponse("Données du fichier importées dans la base PostgreSQL.")  
    
    
def readfileint_function():
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'int.txt')
    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip(): 
                    data = line.strip().split('|')
                    if len(data) >= 4: 
                        try:
                            date_str = data[0].strip()
                            bhTN1 = float(data[1].strip())
                            bhTN2 = float(data[2].strip())
                            bhSO = float(data[3].strip())
                            
                            mm_instance, created = Int.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'bhTN1': bhTN1,
                                    'bhTN2': bhTN2,
                                    'bhSO': bhSO,
                                    
                                }
                            )

                        except (ValueError, IndexError) as e:
                            continue

    else:
        print(f"Fichier non trouvé dans le répertoire spécifié.")

def readfileint(request):
    readfileint_function()
    return HttpResponse("Données du fichier importées dans la base PostgreSQL.")  
    
def readfiletn1epg_function():
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'max_output_filetn1.txt')


    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip(): 
                    data = line.strip().split('|')
                    if len(data) >= 4: 
                        try:
                            date_str = data[0].strip()
                            avg16 = int(data[1].strip())
                            peak16 = int(data[2].strip())
                            avg4 = int(data[3].strip())
                            peak4 = int(data[4].strip())
                            avg5 =int(data[5].strip())
                            peak5 = int(data[6].strip())
                            avg14 = int(data[7].strip())
                            peak14 = int(data[8].strip())
                            avg15 = int(data[9].strip())
                            peak15 = int(data[10].strip())
                            avg17 = int(data[11].strip())
                            peak17 = int(data[12].strip())
                            avg6 = int(data[13].strip())
                            peak6 = int(data[14].strip())
                            actpdpcont = int(data[15].strip())
                            acteps = int(data[16].strip())
                            actsub = int(data[17].strip())
                            
                            mm_instance, created = Tn1EPG.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'avg16': avg16,
                                    'peak16': peak16,
                                    'avg4': avg4,
                                    'peak4': peak4,
                                    'avg5': avg5,
                                    'peak5': peak5,
                                    'avg14': avg14,
                                    'peak14': peak14,
                                    'avg15': avg15,
                                    'peak15': peak15,
                                    'avg17': avg17,
                                    'peak17': peak17,
                                    'avg6': avg6,
                                    'peak6': peak6,
                                    'actpdpcont': actpdpcont,
                                    'acteps': acteps,
                                    'actsub': actsub,
                                    
                                }
                            )

                        except (ValueError, IndexError) as e:
                            # Handle errors if data format is incorrect
                            continue

        return HttpResponse(f"Données du fichier importées dans la base PostgreSQL.")
    else:
        return HttpResponse(f"Fichier  non trouvé dans le répertoire spécifié.")
    
    
def readfiletn1epg(request):
    readfiletn1epg_function()
    return HttpResponse("Données du fichier importées dans la base PostgreSQL.")  
    


def readfiletn2epg_function():
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'max_output_filetn2.txt')


    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip(): 
                    data = line.strip().split('|')
                    if len(data) >= 4: 
                        try:
                            date_str = data[0].strip()
                            avg16 = int(data[1].strip())
                            peak16 = int(data[2].strip())
                            avg5 = int(data[3].strip())
                            peak5 = int(data[4].strip())
                            avg6 =int(data[5].strip())
                            peak6 = int(data[6].strip())
                            avg11 = int(data[7].strip())
                            peak11 = int(data[8].strip())
                            avg12 = int(data[9].strip())
                            peak12 = int(data[10].strip())
                            avg13 = int(data[11].strip())
                            peak13 = int(data[12].strip())
                            avg15 = int(data[13].strip())
                            peak15 = int(data[14].strip())
                            avg17 = int(data[15].strip())
                            peak17 = int(data[16].strip())
                            avg18 = int(data[17].strip())
                            peak18 = int(data[18].strip())
                            avg19 =int(data[19].strip())
                            peak19 = int(data[20].strip())
                            avg2 = int(data[21].strip())
                            peak2 = int(data[22].strip())
                            avg20 = int(data[23].strip())
                            peak20 = int(data[24].strip())
                            avg3 = int(data[25].strip())
                            peak3 = int(data[26].strip())
                            avg4 = int(data[27].strip())
                            peak4 = int(data[28].strip())
                            avg8 = int(data[29].strip())
                            peak8 = int(data[30].strip())
                            avg9 = int(data[31].strip())
                            peak9 = int(data[32].strip())
                            actpdpcont = int(data[33].strip())
                            acteps = int(data[34].strip())
                            actsub = int(data[35].strip())
                            
                            mm_instance, created = Tn2EPG.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'avg16': avg16,
                                    'peak16': peak16,
                                    'avg5': avg5,
                                    'peak5': peak5,
                                    'avg6': avg6,
                                    'peak6': peak6,
                                    'avg11': avg11,
                                    'peak11': peak11,
                                    'avg12': avg12,
                                    'peak12': peak12,
                                    'avg13': avg13,
                                    'peak13': peak13,
                                    'avg15': avg15,
                                    'peak15': peak15,
                                    'avg17': avg17,
                                    'peak17': peak17,
                                    'avg18': avg18,
                                    'peak18': peak18,
                                    'avg19': avg19,
                                    'peak19': peak19,
                                    'avg2': avg2,
                                    'peak2': peak2,
                                    'avg20': avg20,
                                    'peak20': peak20,
                                    'avg3': avg3,
                                    'peak3': peak3,
                                    'avg4': avg4,
                                    'peak4': peak4,
                                    'avg8': avg8,
                                    'peak8': peak8,
                                    'avg9': avg9,
                                    'peak9': peak9,
                                    'actpdpcont': actpdpcont,
                                    'acteps': acteps,
                                    'actsub': actsub,
                                    
                                }
                            )

                        except (ValueError, IndexError) as e:
                            # Handle errors if data format is incorrect
                            continue

        return HttpResponse(f"Données du fichier importées dans la base PostgreSQL.")
    else:
        return HttpResponse(f"Fichier  non trouvé dans le répertoire spécifié.")
    
    
def readfiletn2epg(request):
    readfiletn2epg_function()
    return HttpResponse("Données du fichier importées dans la base PostgreSQL.")  
        
    
    
def readfilesoepg_function():
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'max_output_fileso.txt')


    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip(): 
                    data = line.strip().split('|')
                    if len(data) >= 4: 
                        try:
                            date_str = data[0].strip()
                            avg29 = int(data[1].strip())
                            peak29 = int(data[2].strip())
                            avg30 = int(data[3].strip())
                            peak30 = int(data[4].strip())
                            avg1 =int(data[5].strip())
                            peak1 = int(data[6].strip())
                            avg2 = int(data[7].strip())
                            peak2 = int(data[8].strip())
                            avg3 = int(data[9].strip())
                            peak3 = int(data[10].strip())
                            avg4 = int(data[11].strip())
                            peak4 = int(data[12].strip())
                            avg5 = int(data[13].strip())
                            peak5 = int(data[14].strip())
                            avg6 = int(data[15].strip())
                            peak6 = int(data[16].strip())
                            actpdpcont = int(data[17].strip())
                            acteps = int(data[18].strip())
                            actsub = int(data[19].strip())
                            
                            mm_instance, created = SOEPG.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'avg29':avg29,
                                    'peak29':peak29,
                                    'avg30':avg30,
                                    'peak30':peak30,
                                    'avg1':avg1,
                                    'peak1':peak1,
                                    'avg2':avg2,
                                    'peak2':peak2,
                                    'avg3':avg3,
                                    'peak3':peak3,
                                    'avg4': avg4,
                                    'peak4': peak4,
                                    'avg5': avg5,
                                    'peak5': peak5,
                                    'avg6': avg6,
                                    'peak6': peak6,
                                    'actpdpcont': actpdpcont,
                                    'acteps': acteps,
                                    'actsub': actsub,
                                    
                                }
                            )

                        except (ValueError, IndexError) as e:
                            # Handle errors if data format is incorrect
                            continue

        return HttpResponse(f"Données du fichier importées dans la base PostgreSQL.")
    else:
        return HttpResponse(f"Fichier  non trouvé dans le répertoire spécifié.")
    

def readfilesoepg(request):
    readfilesoepg_function()
    return HttpResponse("Données du fichier importées dans la base PostgreSQL.")  
    
def readfiletn2vepg_function():
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'max_output_filetn2vepg1.txt')


    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip(): 
                    data = line.strip().split('|')
                    if len(data) >= 4: 
                        try:
                            date_str = data[0].strip()
                            avg29 = int(data[1].strip())
                            peak29 = int(data[2].strip())
                            avg30 = int(data[3].strip())
                            peak30 = int(data[4].strip())
                            avg1 =int(data[5].strip())
                            peak1 = int(data[6].strip())
                            avg10 = int(data[7].strip())
                            peak10 = int(data[8].strip())
                            avg11 = int(data[9].strip())
                            peak11 = int(data[10].strip())
                            avg12 = int(data[11].strip())
                            peak12 = int(data[12].strip())
                            avg2 = int(data[13].strip())
                            peak2 = int(data[14].strip())
                            avg3 = int(data[15].strip())
                            peak3 = int(data[16].strip())
                            avg4 = int(data[17].strip())
                            peak4 = int(data[18].strip())
                            avg5 = int(data[19].strip())
                            peak5 = int(data[20].strip())
                            avg6 = int(data[21].strip())
                            peak6 = int(data[22].strip())
                            avg7 = int(data[23].strip())
                            peak7 = int(data[24].strip())
                            avg8 = int(data[25].strip())
                            peak8 = int(data[26].strip())
                            avg9 = int(data[27].strip())
                            peak9 = int(data[28].strip())
                            actpdpcont = int(data[29].strip())
                            acteps = int(data[30].strip())
                            actsub = int(data[31].strip())
                            
                            mm_instance, created = TN2VEPG.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'avg29': avg29,
                                    'peak29': peak29,
                                    'avg30': avg30,
                                    'peak30': peak30,
                                    'avg1': avg1,
                                    'peak1': peak1,
                                    'avg10': avg10,
                                    'peak10': peak10,
                                    'avg11': avg11,
                                    'peak11': peak11,
                                    'avg12': avg12,
                                    'peak12': peak12,
                                    'avg2': avg2,
                                    'peak2': peak2,
                                    'avg3': avg3,
                                    'peak3': peak3,
                                    'avg4': avg4,
                                    'peak4': peak4,
                                    'avg5': avg5,
                                    'peak5': peak5,
                                    'avg6': avg6,
                                    'peak6': peak6,
                                    'avg7': avg7,
                                    'peak7': peak7,
                                    'avg8': avg8,
                                    'peak8': peak8,
                                    'avg9': avg9,
                                    'peak9': peak9,
                                    'actpdpcont': actpdpcont,
                                    'acteps': acteps,
                                    'actsub': actsub,
                                    
                                }
                            )

                        except (ValueError, IndexError) as e:
                            # Handle errors if data format is incorrect
                            continue

        return HttpResponse(f"Données du fichier importées dans la base PostgreSQL.")
    else:
        return HttpResponse(f"Fichier  non trouvé dans le répertoire spécifié.")
   
   
def readfiletn2vepg(request):
    readfiletn2vepg_function()
    return HttpResponse("Données du fichier importées dans la base PostgreSQL.")      

def readfiletn1apn(request):
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'apnresultTN1.txt')


    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip(): 
                    data = line.strip().split('|')
                    if len(data) >= 4: 
                        try:
                            date_str = data[0].strip()
                            weborangetn1 = float(data[1].strip())
                            keyprotn1 = float(data[2].strip())
                            keygptn1 = float(data[3].strip())
                            dataltetddtn1 = float(data[4].strip())
                            geoloctn1 = float(data[5].strip())
                            keybusinesstn1 = float(data[6].strip())
                            
                            
                            mm_instance, created = Tn1APN.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'weborangetn1':weborangetn1,
                                    'keyprotn1':keyprotn1,
                                    'keygptn1':keygptn1,
                                    'dataltetddtn1':dataltetddtn1,
                                    'geoloctn1':geoloctn1,
                                    'keybusinesstn1':keybusinesstn1,
                                    
                                    
                                }
                            )

                        except (ValueError, IndexError) as e:
                            # Handle errors if data format is incorrect
                            continue

        return HttpResponse(f"Données du fichier importées dans la base PostgreSQL.")
    else:
        return HttpResponse(f"Fichier  non trouvé dans le répertoire spécifié.")
    

def readfilesoapn(request):
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'apnresultSO.txt')


    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip(): 
                    data = line.strip().split('|')
                    if len(data) >= 2: 
                        try:
                            date_str = data[0].strip()
                            weborangeso = float(data[1].strip())
                            flyboxgpso = float(data[2].strip())
                            
                            
                            mm_instance, created = SOAPN.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'weborangeso': weborangeso,
                                    'flyboxgpso': flyboxgpso,
                                    
                                }
                            )

                        except (ValueError, IndexError) as e:
                            # Handle errors if data format is incorrect
                            continue

        return HttpResponse(f"Données du fichier importées dans la base PostgreSQL.")
    else:
        return HttpResponse(f"Fichier  non trouvé dans le répertoire spécifié.")
    
def readfiletn2apn(request):
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'apnresultTN2.txt')


    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip(): 
                    data = line.strip().split('|')
                    if len(data) >= 4: 
                        try:
                            date_str = data[0].strip()
                            weborangetn2 = float(data[1].strip())
                            keygptn2 = float(data[2].strip())
                            dataltetddtn2 = float(data[3].strip())
                            geoloctn2 = float(data[4].strip())
                            keybusinesstn2 = float(data[5].strip())
                            
                            mm_instance, created = Tn2APN.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'weborangetn2':weborangetn2,
                                    'keygptn2':keygptn2,
                                    'dataltetddtn2':dataltetddtn2,
                                    'geoloctn2':geoloctn2,
                                    'keybusinesstn2':keybusinesstn2,
                                    
                                    
                                }
                            )

                        except (ValueError, IndexError) as e:
                            # Handle errors if data format is incorrect
                            continue

        return HttpResponse(f"Données du fichier importées dans la base PostgreSQL.")
    else:
        return HttpResponse(f"Fichier  non trouvé dans le répertoire spécifié.")
def readfiletn2vepgapn(request):
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'apnresultTN2vEPG.txt')


    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip(): 
                    data = line.strip().split('|')
                    if len(data) >= 1: 
                        try:
                            date_str = data[0].strip()
                            weborangetn2vepg = float(data[1].strip())
                            keyprotn2vepg = float(data[2].strip())
                            flyboxgptn2vepg = float(data[3].strip())
                            flyboxprotn2vepg = float(data[4].strip())
                            dataltetddtn2vepg = float(data[5].strip())
                            
                            
                            mm_instance, created = Tn2VEPGAPN.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'weborangetn2vepg': weborangetn2vepg,
                                    'keyprotn2vepg': keyprotn2vepg,
                                    'flyboxgptn2vepg': flyboxgptn2vepg,
                                    'flyboxprotn2vepg': flyboxprotn2vepg,
                                    'dataltetddtn2vepg': dataltetddtn2vepg,

                                    
                                }
                            )

                        except (ValueError, IndexError) as e:
                            # Handle errors if data format is incorrect
                            continue

        return HttpResponse(f"Données du fichier importées dans la base PostgreSQL.")
    else:
        return HttpResponse(f"Fichier  non trouvé dans le répertoire spécifié.")




from django.shortcuts import render

def mme_view(request):
    tn1_data = Tn1MME.objects.all().order_by('-date')
    tn2_data = Tn2MME.objects.all().order_by('-date')
    sousse_data = SoMME.objects.all().order_by('-date')
    
    
    context = {
        'tn1_data': tn1_data,
        'tn2_data': tn2_data,
        'sousse_data': sousse_data,
    }
    return render(request, 'MMEomea.html',context)

def int_view(request):
    int_data = Int.objects.all().order_by('-date')
    
    context = {
        'int_data': int_data,
        
    }
    return render(request, 'MMEint.html',context)

def global_view(request):
    tn1global_data = Tn1MME.objects.all().order_by('-date')
    tn2global_data = Tn2MME.objects.all().order_by('-date')
    sousseglobal_data = SoMME.objects.all().order_by('-date')
    
    
    context = {
        
        'tn1global_data': tn1global_data,
        'tn2global_data': tn2global_data,
        'sousseglobal_data': sousseglobal_data,
        
    }
    return render(request, 'MMEglobal.html',context)

def epg_view(request):
    tn1epg_data = Tn1EPG.objects.all().order_by('-date')
    tn2epg_data = Tn2EPG.objects.all().order_by('-date')
    tn2vepg_data = TN2VEPG.objects.all().order_by('-date')
    soepg_data = SOEPG.objects.all().order_by('-date')
    
    context = {
        'tn1epg_data': tn1epg_data,
        'tn2epg_data': tn2epg_data,
        'tn2vepg_data': tn2vepg_data,
        'soepg_data': soepg_data,

    }
    return render(request, 'epg.html',context)

def apn_view(request):
    tn1apn_data = Tn1APN.objects.all().order_by('-date')
    tn2vepgapn_data = Tn2VEPGAPN.objects.all().order_by('-date')
    soapn_data = SOAPN.objects.all().order_by('-date')
    tn2apn_data= Tn2APN.objects.all().order_by('-date')
    
    context = {
        'tn1apn_data': tn1apn_data,
        'tn2vepgapn_data': tn2vepgapn_data,
        'soapn_data': soapn_data,
        'tn2apn_data': tn2apn_data,

    }
    return render(request, 'apn.html',context)
