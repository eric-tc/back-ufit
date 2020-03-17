from ufit import db

class Utente(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    nome= db.Column(db.String(100),nullable=False)
    cognome = db.Column(db.String(100), nullable=False)
    email= db.Column(db.String(100),nullable=False,unique=True)
    stile_vita = db.Column(db.String(100), nullable=False)
    cellulare = db.Column(db.String(100), nullable=False)
    motivo= db.Column(db.Text())
    aspettativa=db.Column(db.Text())
    servizio=db.Column(db.Text())

    # RELAZIONE ALLENAMNETO

    #Trovare tutti gli allenmenti di un user_id

    #user=User.query.filter_by(nome="nome_da_cercare").first()
    #user.allenamento-> ritorna tutti gli allenamenti assegnati all'utente

    #author serve per trovare l'utente a cui e associato allenamento
    #allenamento=db.relationship('Allenamento',backref='author',lazy=True)

    # SERVE per ritornare tutte le schede associate ad un singolo utente

    scheda=db.relationship('CreaScheda',backref='autore',lazy=True)

    allenamenti= db.relationship('CreaAllenamento',backref="allenamenti",lazy=True)


    # SALUTE
    # i valori di salute sono associati all'utente in fase di creazione della tabella



    infortunio=db.Column(db.String(500), nullable=False)
    malattie=db.Column(db.String(500), nullable=False)
    allenamento_desiderato=db.Column(db.String(500), nullable=False)


    n_all_settimana=db.Column(db.String(100), nullable=False)

    ore_allenamento=db.Column(db.String(100),nullable=False)


    somatotipo = db.Column(db.String(500), nullable=False)

    # descrive il tipo di allenamento gia pratica palestra/nuoto ecc...
    allenamento_praticato = db.Column(db.String(500), nullable=False)



    # infortunio_spalla = db.Column(db.Boolean,default=False)
    # infortunio_gomiti = db.Column(db.Boolean,default=False)
    # infortunio_schiena = db.Column(db.Boolean,default=False)
    #
    # malattie_cardiovascolari = db.Column(db.Boolean,default=False)
    # malattie_metaboliche = db.Column(db.Boolean,default=False)
    # malattie_reumatiche = db.Column(db.Boolean,default=False)
    # malattie_neurodegenerative = db.Column(db.Boolean,default=False)
    #
    # allenamento_spalle = db.Column(db.Boolean,default=False)
    # allenamento_pesi_liberi = db.Column(db.Boolean,default=False)
    # allenamento_corpo_libero = db.Column(db.Boolean,default=False)
    # allenamento_corpo_libero_elastici = db.Column(db.Boolean,default=False)

    def __repr__(self):

        return f"Utente('{self.id}','{self.nome}','{self.somatotipo}','{self.ore_allenamento}','{self.n_all_settimana}'" \
               f",'{self.allenamento_praticato}')"
    
    def as_dict(self):
           return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    
# class Allenamento(db.Model):
#
#     # Tiene traccia di tutte le schede create dal sistema
#     id_scheda=db.Column(db.Integer,primary_key=True)
#     #Aggiungere un campo versione demo o reale per permettere all'utente di effettuare delle prove
#     demo = db.Column(db.Boolean,default=False)
#
#     #relazione con la tabella utente
#
#     # Esempio database
#
#     # allenamento= Allenamento.query.first()-> ritorna il primo allenamento inserito
#     # allenamento.user_id-> rappresenta il campo user_id della tabella Allenamento
#
#     # utente.id / nome_tabella.nome_campo
#     user_id=db.Column(db.Integer,db.ForeignKey('utente.id'),nullable=False)
#
#     # PETTORALI
#
#     pettorali_pesi_liberi_panca_piana = db.Column(db.Boolean,default=False)
#     pettorali_pesi_liberi_croci_cavi_alti = db.Column(db.Boolean,default=False)
#     pettorali_pesi_liberi_distensioni = db.Column(db.Boolean,default=False)
#
#     pettoriali_macchine_isotoniche_panca_piana = db.Column(db.Boolean,default=False)
#     pettoriali_macchine_isotoniche_croci_cavi_alti = db.Column(db.Boolean,default=False)
#     pettoriali_macchine_isotoniche_distensioni = db.Column(db.Boolean,default=False)
#
#
#     pettoriali_corpo_libero_panca_piana = db.Column(db.Boolean,default=False)
#     pettoriali_corpo_libero_croci_cavi_alti = db.Column(db.Boolean,default=False)
#     pettoriali_corpo_libero_distensioni = db.Column(db.Boolean,default=False)
#
#     # DORSALI
#
#     dorsali_pesi_liberi_panca_piana = db.Column(db.Boolean,default=False)
#     dorsali_pesi_liberi_croci_cavi_alti = db.Column(db.Boolean,default=False)
#     dorsali_pesi_liberi_distensioni = db.Column(db.Boolean,default=False)
#
#     dorsali_macchine_istoniche_panca_piana = db.Column(db.Boolean,default=False)
#     dorsali_macchine_istoniche_croci_cavi_alti = db.Column(db.Boolean,default=False)
#     dorsali_macchine_istoniche_distensioni = db.Column(db.Boolean,default=False)
#
#     dorsali_corpo_libero_panca_piana = db.Column(db.Boolean,default=False)
#     dorsali_corpo_libero_croci_cavi_alti = db.Column(db.Boolean,default=False)
#     dorsali_corpo_libero_distensioni = db.Column(db.Boolean,default=False)
#
#     # SPALLE
#     spalle_pesi_liberi_panca_piana = db.Column(db.Boolean,default=False)
#     spalle_pesi_liberi_croci_cavi_alti = db.Column(db.Boolean,default=False)
#     spalle_pesi_liberi_distensioni = db.Column(db.Boolean,default=False)
#
#     spalle_macchine_isotoniche_panca_piana = db.Column(db.Boolean,default=False)
#     spalle_macchine_isotoniche_croci_cavi_alti = db.Column(db.Boolean,default=False)
#     spalle_macchine_isotoniche_distensioni = db.Column(db.Boolean,default=False)
#
#     spalle_corpo_libero_panca_piana = db.Column(db.Boolean,default=False)
#     spalle_corpo_libero_croci_cavi_alti = db.Column(db.Boolean,default=False)
#     spalle_corpo_libero_distensioni = db.Column(db.Boolean,default=False)
#
#
#     # BICIPITI
#
#     bicipiti_pesi_liberi_panca_piana = db.Column(db.Boolean,default=False)
#     bicipiti_pesi_liberi_croci_cavi_alti = db.Column(db.Boolean,default=False)
#     bicipiti_pesi_liberi_distensioni = db.Column(db.Boolean,default=False)
#
#     bicipiti_macchine_isotoniche_panca_piana = db.Column(db.Boolean,default=False)
#     bicipiti_macchine_isotoniche_croci_cavi_alti = db.Column(db.Boolean,default=False)
#     bicipiti_macchine_isotoniche_distensioni = db.Column(db.Boolean,default=False)
#
#     bicipiti_corpo_libero_panca_piana = db.Column(db.Boolean,default=False)
#     bicipiti_corpo_libero_croci_cavi_alti = db.Column(db.Boolean,default=False)
#     bicipiti_corpo_libero_distensioni = db.Column(db.Boolean,default=False)

class Allenamento(db.Model):

    """
    Tabella in cui saranno elencati tutti gli allenamenti
    
    """

    id_allenamento=db.Column(db.Integer,primary_key=True)

    nome_allenamento=db.Column(db.String(100),nullable=False)

    def __repr__(self):

        return f"Allenamento('{self.id_allenamento}','{self.nome_allenamento}')"
    
    def as_dict(self):
           return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class CreaScheda(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    # indica se la scheda e allenamento riscaldamento o post allenamento
    tipologia=db.Column(db.String(20),nullable=False)

    # fa riferimento all utente a cui e associta la scheda

    id_utente=db.Column(db.Integer,db.ForeignKey('utente.id'),nullable=False)

    # Serve per ritornare tutti gli allenamenti associati alla singola scheda

    allenamenti=db.relationship('CreaAllenamento',backref="allenamento",lazy=True)

    # durata scheda

    durata = db.Column(db.String(100), nullable=False)

    # tipo di programmazione

    tipo_programmazione= db.Column(db.String(100),nullable=False)

    # tipo di carico

    tipo_carico = db.Column(db.String(100), nullable=False)


    def __repr__(self):

        return f"CreaScheda('{self.id}','{self.tipologia}','{self.durata}','{self.tipo_programmazione}'," \
               f"'{self.tipo_carico}')"

class CreaAllenamento(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    # collegamento con id della scheda
    id_scheda=db.Column(db.Integer,db.ForeignKey("crea_scheda.id"),nullable=False)

    #collegamento con id utente
    id_utente=db.Column(db.Integer,db.ForeignKey("utente.id"),nullable=False)


    # numero di ripetizioni per il singolo allenamento
    ripetizioni=db.Column(db.String(20),nullable=False)
    # indica se esercizio appartiente ad un circuito
    circuito=db.Column(db.String(20),nullable=False)
    #gestisce la pausa tra un allenamento e l'altro
    pausa_allenamento=db.Column(db.String(20),nullable=False)
    # indica quando eseguire esercizio
    posizione_esercizio=db.Column(db.String(20),nullable=False)

    nome_allenamento=db.Column(db.String(100),nullable=False)

    discriminanti_esercizi=db.Column(db.String(100),nullable=False)

    tipo_di_lavoro=db.Column(db.String(100),nullable=False)

    contrazione_richiesta=db.Column(db.String(100),nullable=False)


    serie=db.Column(db.String(100),nullable=False)

    # identifica la tipologia di allenamento
    numero_allenamento=db.Column(db.String(100),nullable=False)
    # esercizio di rilassamento tra un esercizio e il successivo
    esercizi_rilassamento=db.Column(db.String(100),nullable=False)




    def __repr__(self):

        # riuscire a ritornare i dati con una query devo inserire tutti i campi
        return f"CreaAllenamento('{self.id}','{self.id_scheda}','{self.id_utente}'" \
               f",'{self.circuito}','{self.pausa_allenamento}','{self.posizione_esercizio}'" \
               f",'{self.ripetizioni}','{self.nome_allenamento}','{self.discriminanti_esercizi}'," \
               f"'{self.tipo_di_lavoro}','{self.contrazione_richiesta}','{self.serie}','{self.numero_allenamento}'," \
               f"'{self.esercizi_rilassamento}')"









