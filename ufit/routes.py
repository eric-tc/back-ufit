from flask import render_template, flash, redirect, url_for,make_response,jsonify,request
from ufit import app, db,generazione_scheda
from ufit.forms import GeneralInput, CreaAllenamentoForm,DynamicForm,CreaSchedaForm
from ufit.models import Utente, CreaScheda,Allenamento,CreaAllenamento

from wtforms import StringField
from wtforms.validators import DataRequired,Length


import datetime

import time

import pdfkit

import numpy as np

# id della scheda creata
gloab_scheda_id=None


# variabile creazione scheda
# questa variabile verfica se e stato generato il pdf della scheda


@app.route("/test",methods=["GET"])
def test_route():

    return jsonify("test")





@app.route('/new-client', methods=['GET', 'POST','PUT'])
def new_client():
    # importo il form nell html della pagina

    

    client_form = GeneralInput()

    #gestion risposta da Vue
    
    if request.method=="POST":
        
        print(request.get_json())
        #input("DATA JSON")
        
        client_form=request.get_json()
        
        user = Utente(nome=client_form["name"], cognome="campo", email=client_form["email"],
                                    cellulare=client_form["cellulare"], stile_vita=client_form["stileVita"],
                                    motivo=client_form["motivoRichiesta"], aspettativa=client_form["aspettativaServizio"],
                                    servizio=client_form["aspettativaServizio"],infortunio=client_form["infortunio"],malattie=client_form["malattie"],
                                    allenamento_desiderato=client_form["allenamentoDesiderato"],somatotipo=client_form["somatotipo"],
                                    allenamento_praticato=client_form["allenamentoSvolto"],n_all_settimana=client_form["numAllenamenti"],
                                    ore_allenamento=client_form["oreDisponibili"])

        
        db.session.add(user)

        db.session.commit()
        
        list_dict={"success":"True"}
        
        return jsonify(list_dict)

        
        
    
    
    # quando l'utente esegue il comando on submit
    print ("PRE_VALIDATE")
    print (client_form.validate_on_submit())
    if client_form.validate_on_submit():
        # Dati dal form
        # nome_istanza.nome_campo.data
        # client_general_info.username.data
        # flash('dati inseriti correttamente {}'.format(client_general_info.username.data),'success')

        # success rappresenta la classe di bootstrap da passare alla visualizzazione
        flash('Dati inseriti correttamente. Ora crea Allenamento per Utente {}'.format(client_form.username.data),
              'success')

        print ('VALIDATE')


        # ritorna spalla
        # print (client_general_info.infortuni.data[0])
        print ("INFORTUNIO")


        # inserisco i dati a database

        # user = Utente(nome=client_form.username.data, cognome=client_form.surname.data, email=client_form.email.data,
        #               cellulare=client_form.cellulare.data, stile_vita=client_form.stile_di_vita.data,
        #               motivo=client_form.motivo.data, aspettativa=client_form.aspettativa.data,
        #               servizio=client_form.servizio.data,
        #               infortunio_spalla=True if 'spalle' in client_form.infortuni.data else False,
        #               infortunio_gomiti=True if 'gomiti' in client_form.infortuni.data else False,
        #               infortunio_schiena=True if 'schiena' in client_form.infortuni.data else False,
        #               malattie_cardiovascolari=True if 'cardiovascolari' in client_form.malattie.data else False,
        #               malattie_metaboliche=True if 'metaboliche' in client_form.malattie.data else False,
        #               malattie_reumatiche=True if 'reumatiche' in client_form.malattie.data else False,
        #               malattie_neurodegenerative=True if 'neurodegenerative' in client_form.malattie.data else False,
        #               allenamento_spalle=True if 'all_spalle' in client_form.allenamento_desiderato.data else False,
        #               allenamento_pesi_liberi=True if 'pesi_liberi' in client_form.allenamento_desiderato.data else False,
        #               allenamento_corpo_libero=True if 'corpo_libero' in client_form.allenamento_desiderato.data else False,
        #               allenamento_corpo_libero_elastici=True if 'corpo_libero_elastici' in client_form.allenamento_desiderato.data else False)

        user = Utente(nome=client_form.username.data, cognome=client_form.surname.data, email=client_form.email.data,
                                    cellulare=client_form.cellulare.data, stile_vita=client_form.stile_di_vita.data,
                                    motivo=client_form.motivo.data, aspettativa=client_form.aspettativa.data,
                                    servizio=client_form.servizio.data,infortunio=client_form.infortuni.data,malattie=client_form.malattie.data,
                                    allenamento_desiderato=client_form.allenamento_desiderato.data,somatotipo=client_form.somatotipo.data,
                                    allenamento_praticato=client_form.allenamento_praticato.data,n_all_settimana=client_form.n_all_settimana.data,
                                    ore_allenamento=client_form.ore_allenamento.data)



        # user=Utente(nome=client_form.username.data)

        # Aggiungo Utente
        db.session.add(user)

        db.session.commit()

        # prendo id utente generato


        # passo alla pagina crea allenamento

        # user_id rappresenta il parametro passato alla pagina crea_allenamento
        return redirect(url_for('list_client'))

    return render_template('NewClient.html', title='New', form=client_form)



@app.route('/scelta-esercizi/<int:user_id>/<int:scheda_id>',methods=['GET', 'POST'])
def scelta_esercizi(user_id,scheda_id):

    # funzione per selezionare gli esercizi







    allenamento_form = CreaAllenamentoForm()



    if allenamento_form.validate_on_submit():

        # array che contiene solo gli esercizi selezionati
        array_esercizi=[]
        #print (allenamento_form.pettorali.data)

        # inserisco tutti gli id selezionati nell array

        for element in allenamento_form.pettorali.data:

            array_esercizi.append(element)

        for element in allenamento_form.spalle.data:
            array_esercizi.append(element)

        for element in allenamento_form.dorsali.data:
            array_esercizi.append(element)

        for element in allenamento_form.bicipiti.data:
            array_esercizi.append(element)


        for element in allenamento_form.bicipiti.data:
            array_esercizi.append(element)

        for element in allenamento_form.tricipiti.data:
            array_esercizi.append(element)

        for element in allenamento_form.addominali.data:
            array_esercizi.append(element)

        for element in allenamento_form.dorsali_posturali.data:
            array_esercizi.append(element)

        for element in allenamento_form.quadricipiti.data:
            array_esercizi.append(element)

        for element in allenamento_form.flessori_ginocchio.data:
            array_esercizi.append(element)

        for element in allenamento_form.estensori_anca.data:
            array_esercizi.append(element)

        for element in allenamento_form.polpacci.data:
            array_esercizi.append(element)

        for element in allenamento_form.adduttori.data:
            array_esercizi.append(element)

        for element in allenamento_form.abduttori.data:
            array_esercizi.append(element)

        print ("GENERAZIONE SCHEDA")
        print (array_esercizi)
        return redirect(url_for('crea_allenamento', user_id=user_id, scheda_id=scheda_id,array_esercizi=array_esercizi))



    return render_template('SceltaEsercizi.html',form_allenamento=allenamento_form)





    
    

@app.route('/crea-scheda/<int:user_id>',methods=['GET', 'POST'])
def crea_scheda(user_id):

    """
    gestisce la pagina di creazione delle caratteristiche della scheda
    
    :param user_id:ritorna id utente 
    :return: 
    """
    # form per scegliere gli esercizi





    form_crea_scheda=CreaSchedaForm()



    print (form_crea_scheda.validate_on_submit())
    if form_crea_scheda.validate_on_submit():



        print (form_crea_scheda.data._value())

        timestamp=form_crea_scheda.data._value()

        timestamp= timestamp.split("/")

        print (timestamp)

        timestamp=datetime.date(int(timestamp[2]),int(timestamp[0]),int(timestamp[1]))


        unixtime= time.mktime(timestamp.timetuple())

        print (unixtime)




        scheda = CreaScheda(id_utente=user_id, tipologia=1,tipo_programmazione=form_crea_scheda.tipo_programmazione.data,
                            tipo_carico=form_crea_scheda.tipo_carico.data,durata=form_crea_scheda.data.data)


        db.session.add(scheda)

        db.session.commit()


        return redirect(
            url_for('scelta_esercizi', user_id=user_id, scheda_id=scheda.id))






        #return redirect(url_for('crea_allenamento', user_id=user_id, scheda_id=gloab_scheda_id,array_esercizi=array_esercizi))


    # devo inserire una scheda a database con associtato id utente e la tipologia della scheda




    # al template devo passare anche id della scheda appena creata a cui saranno associtati gli allenamenti
    # gli passo anche id dell'utente







    #     scheda = CreaScheda(id_utente=user_id, tipologia=1)
    #
    #     db.session.add(scheda)
    #     print ("Commit")
    #     db.session.commit()
    #
    #     # id acquisto solo dopo il commit
    #     gloab_scheda_id = scheda.id
    #
    #     # variabile che non permette la creazione di una nuova scheda fintanto che
    #     # non ho creato il pdf di quella precedente
    #     generazione_scheda=1
    #
    #     print("GENERAZIONE SCHEDA INSIDE")
    #
    # print("GENERAZIONE SCHEDA OUTSIDE")
    # print (generazione_scheda)

    # DA SOSTITUIRE CON scheda.id
    return render_template('CreaScheda.html',user_id=user_id,form_crea_scheda=form_crea_scheda)







@app.route('/crea-allenamento/<int:user_id>/<scheda_id>/<string:array_esercizi>',methods=['GET', 'POST'])
def crea_allenamento(user_id,scheda_id,array_esercizi):
    # ritorna il valore di user_id

    # utilizzata per creare il form dinamico
    class F(DynamicForm):
        pass

    print(user_id)
    print ("allenamento")

    #record = {'field1': 'label1', 'field2': 'label2'}

    # dizionario {"id_allenamento": "nome allenamento"}
    record={}

    # recupero gli allenamenti

    lista_allenamenti = Allenamento.query.all()


    print ("CREA ALLENAMENTO")
    print (array_esercizi)

    # devo convertire la stringa in array altrimenti il valore '2' se la stringa
    # e ['12'] da come risultato True
    string_to_array = array_esercizi.replace(']', '').replace('[', '')
    string_to_array= string_to_array.replace("'", '').replace(' ', '').split(",")

    print (len(string_to_array))

    for allenamento in lista_allenamenti:

        # verifico che esercizio sia presente nella lista degli esercizi selezionati
        if str(allenamento.id_allenamento) in string_to_array:
            print (allenamento.id_allenamento)
            #record['{}'.format(str(allenamento.id_allenamento))]= record['{}'.format(str("prova"))]
            record.update({'-{}'.format(str(allenamento.id_allenamento)):'{}'.format(str(allenamento.nome_allenamento))})
            print ("TRUE")
    print ("ID")

    #print (lista_allenamenti[0].id_allenamento)

    print (record)

    for key,value in record.items():
        # la key deve essere diversa per ciascun elemento per essere visualizzato
        setattr(F, str("1{}".format(key)) ,StringField(default=str("{}").format(value),validators=[DataRequired(),Length(min=1,max=1000)]))
        setattr(F, str("2{}".format(key)),StringField(default=str("numero_allenamento"), validators=[DataRequired(), Length(min=1, max=1000)]))
        setattr(F, str("3{}".format(key)),StringField(default=str("Circuito"), validators=[DataRequired(), Length(min=1, max=1000)]))
        setattr(F, str("4{}".format(key)),StringField(default=str("posizione"), validators=[DataRequired(), Length(min=1, max=1000)]))
        setattr(F, str("5{}".format(key)), StringField(default=str("numero"), validators=[DataRequired(), Length(min=1, max=1000)]))
        setattr(F, str("6{}".format(key)),StringField(default=str("serie"), validators=[DataRequired(), Length(min=1, max=1000)]))
        setattr(F, str("7{}".format(key)), StringField(default=str("pausa_allenamento"), validators=[DataRequired(), Length(min=1, max=1000)]))
        setattr(F, str("8{}".format(key)),StringField(default=str("tipo_lavoro"), validators=[DataRequired(), Length(min=1, max=1000)]))
        setattr(F, str("9{}".format(key)),StringField(default=str("contrazione"), validators=[DataRequired(), Length(min=1, max=1000)]))
        setattr(F, str("10{}".format(key)), StringField(default=str("discriminanti"), validators=[DataRequired(), Length(min=1, max=1000)]))
        setattr(F, str("11{}".format(key)), StringField(default=str("esercizi_rilassamento"), validators=[DataRequired(), Length(min=1, max=1000)]))

    print ("CREA ALLENAMENTO")
    print (array_esercizi)


    form_dynamic=F()


    # Quando ritornano i valori dal form

    if form_dynamic.validate_on_submit():

        print(form_dynamic.data)
        print ("Submission Form")

        #str = '["Foo","Bar","Baz","Woo"]'

        # conversione da stringa ad array
        array_esercizi = array_esercizi.replace(']', '').replace('[', '')
        l = array_esercizi.replace("'", '').replace(' ','').split(",")
        print ("ARRAY")
        print (l)
        print (len(l))

        # conversione string array

        nome_allenamento=None
        ripetizioni=None
        circuito=None
        pausa=None
        posizione=None
        discriminanti=None
        contrazione=None
        tipo_lavoro=None
        serie=None
        numero_allenamento=None
        esericizi_rilassamento=None


        for esercizio in l:

            print('ESERCIZIO')
            print (esercizio)


            # ciclo attraverso tutti i valori del singolo esercizio
            for i in range(1,13,1):

                if i==1:

                    nome_allenamento=form_dynamic.data['{}-{}'.format(i,esercizio)]
                if i==2:
                    numero_allenamento = form_dynamic.data['{}-{}'.format(i, esercizio)]

                if i==3:
                    circuito=form_dynamic.data['{}-{}'.format(i,esercizio)]
                if i==4:
                    posizione = form_dynamic.data['{}-{}'.format(i, esercizio)]

                if i==5:
                    ripetizioni = form_dynamic.data['{}-{}'.format(i, esercizio)]
                if i==6:
                    serie = form_dynamic.data['{}-{}'.format(i, esercizio)]

                if i==7:
                    pausa = form_dynamic.data['{}-{}'.format(i, esercizio)]

                if i==8:
                    tipo_lavoro = form_dynamic.data['{}-{}'.format(i, esercizio)]
                if i==9:
                    contrazione = form_dynamic.data['{}-{}'.format(i, esercizio)]
                if i==10:
                    discriminanti = form_dynamic.data['{}-{}'.format(i, esercizio)]
                if i==11:
                    esericizi_rilassamento = form_dynamic.data['{}-{}'.format(i, esercizio)]





            # dopo ogni iterazione inserisco la stringa a database

            inserisci_allenamento=CreaAllenamento(id_scheda=scheda_id,id_utente=user_id,ripetizioni=ripetizioni,
                                                  circuito=circuito,pausa_allenamento=pausa,posizione_esercizio=posizione,
                                                  nome_allenamento=nome_allenamento,discriminanti_esercizi=discriminanti,
                                                  tipo_di_lavoro=tipo_lavoro,contrazione_richiesta=contrazione,serie=serie,
                                                  numero_allenamento=numero_allenamento,esercizi_rilassamento=esericizi_rilassamento)

            db.session.add(inserisci_allenamento)

            db.session.commit()

            # passo al template di generazione del pdf


        return redirect(url_for('generate_pdf', scheda_id=scheda_id))







    return render_template('CreaAllenamento.html',form_dynamic=form_dynamic)

@app.route('/generate-pdf/<scheda_id>')
def generate_pdf(scheda_id):

    """
    
    
    :param scheda_id: id della scheda a cui sono associati gli esercizi 
    :return: 
    """
    print(scheda_id)
    allenamenti = CreaAllenamento.query.filter_by(id_scheda='{}'.format(scheda_id)).order_by(CreaAllenamento.numero_allenamento.asc(),CreaAllenamento.circuito.asc(),CreaAllenamento.posizione_esercizio.asc()).all()

    global generazione_scheda

    generazione_scheda=0

    print (allenamenti[0])

    #return render_template("Pdf.html",allenamenti=allenamenti)
    render=render_template("Pdf.html",allenamenti=allenamenti)

    pdf= pdfkit.from_string(render,False)

    response=make_response(pdf)

    response.headers['Content-Type']='application/pdf'
    response.headers['Content-Disposition']='attachment; filename=output.pdf'

    return response


@app.route('/test-vue')
def test_app():
    return jsonify('pong')

@app.route('/profile/<int:user_id>')
def profile(user_id):
    """
    pagina che gestisce il profilo utente
    
    :return: 
    """
    return render_template('Profilo.html', user_id=user_id)



@app.route('/')
def list_client():
    users = Utente.query.all()

    print(users)
    list_dict=[]

    for user in users:
        dict_user=user.as_dict()
        list_dict.append(dict_user)

    #return render_template('ClientList.html', users=users)
    return jsonify(list_dict)



@app.route('/esercizi',methods=['GET', 'POST'])
def esercizi_allenamento():
    
    lista_allenamenti = Allenamento.query.all()
    
    list_dict=[]
    
    for allenamento in lista_allenamenti:
        dict_allenamento=allenamento.as_dict()
        list_dict.append(dict_allenamento) 
     
    return jsonify(list_dict)