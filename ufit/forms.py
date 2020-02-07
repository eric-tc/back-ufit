from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectMultipleField,SelectField,IntegerField,DateField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError

from wtforms.widgets import ListWidget, CheckboxInput
from ufit.models import Utente


class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()


class FormProject(FlaskForm):
    Code = StringField('Code', [DataRequired(message='Please enter your code')])
    Tasks = MultiCheckboxField('Proses', [DataRequired(message='Please tick your task')], choices=[('nyapu','Nyapu'), ('ngepel','Ngepel')])



class GeneralInput(FlaskForm):

    username= StringField('Username',
                          validators=[DataRequired(),Length(min=1,max=100)])

    surname= StringField('Surname',
                          validators=[DataRequired(),Length(min=1,max=100)])

    stile_di_vita = SelectField(' Stile di Vita', choices=[('attivo', 'Attivo'), ('mediamente', 'Mediamente'), ('sedentario', 'Sedentario')])



    email = StringField('Email',
                           validators=[DataRequired(), Email()])

    cellulare = StringField('Cellulare',
                           validators=[DataRequired(), Length(min=1, max=20)])

    motivo= StringField('Perche ti sei rivolto a me',
                           validators=[DataRequired(), Length(min=1, max=500)])
    aspettativa = StringField('Come pensi ti possa aiutare ',
                           validators=[DataRequired(), Length(min=1, max=500)])
    servizio = StringField('Cosa ti aspetti dal mio servizio',
                           validators=[DataRequired(), Length(min=1, max=500)])

    # Stato di salute


    infortuni = StringField('Descrivere eventuali infortuni',
                           validators=[DataRequired(), Length(min=1, max=500)])

    malattie = StringField('Descrivere le malattie',
                            validators=[DataRequired(), Length(min=1, max=500)])

    allenamento_desiderato = StringField('Descrivere allenamento desiderato',
                            validators=[DataRequired(), Length(min=1, max=500)])

    allenamento_praticato = StringField('Descrivere allenamento che si sta svolgendo',
                                         validators=[DataRequired(), Length(min=1, max=500)])

    somatotipo = StringField('Descrivere il somatotipo',
                                         validators=[DataRequired(), Length(min=1, max=500)])

    ore_allenamento = StringField('Descrivere ore disponibili per allenamento',
                                         validators=[DataRequired(), Length(min=1, max=500)])

    n_all_settimana = StringField('Descrivere in numero quanti allenamenti alla settimana',
                                         validators=[DataRequired(), Length(min=1, max=500)])

    # infortuni = MultiCheckboxField('Infortuni',
    #                            choices=[('spalle', 'Spalle'), ('ginocchia', 'Ginocchia'),
    #                                     ('gomiti', 'Gomiti'),('schiena', 'Schiena')
    #                                     ])
    #
    # malattie = MultiCheckboxField('Malattie',
    #                                choices=[('cardiovascolari', 'Cardiovascolari'), ('metaboliche', 'Metaboliche'),
    #                                         ('reumatiche', 'Reumatiche'), ('neurodegenerative', 'Neurodegenerative')
    #                                         ])
    #
    #
    # allenamento_desiderato = MultiCheckboxField('Allenamento desiderato',
    #                                choices=[('all_spalle', 'Spalle'), ('pesi_liberi', 'Pesi Liberi'),
    #                                         ('corpo_libero', 'Corpo Libero'), ('corpo_libero_elastici', 'Corpo Libero Elastici')
    #                                         ])


    submit=SubmitField('Submit')


    def validate_email(self,email):

        # verifica prima di inserire a database se una mail esiste
        #prendo ultima email inserita
        email= Utente.query.filter_by(email=email.data).first()
        if email:

            raise ValidationError('Email esistente. Cambia email')

class CreaSchedaForm(FlaskForm):

    # tempo di durata della scheda
    data = DateField('Data Fine Scheda', format="%m/%d/%Y")
    # 3:1 ecc
    tipo_programmazione= StringField('Descrivere programmazione scheda',
                                         validators=[DataRequired(), Length(min=1, max=500)])

    tipo_carico=  StringField('Descrivere il tipo di carico',
                                         validators=[DataRequired(), Length(min=1, max=500)])


    submit = SubmitField('Crea Scheda')



class CreaAllenamentoForm(FlaskForm):

    pettorali = MultiCheckboxField('',
                                   choices=[('1', 'Pettoriali Chest Press'), ('2', 'Pettoriali Pectoral machine'),
                                            ('3', 'Pettoriali Panca Piana '), ('4', 'Pettoriali Distensioni Manubri'),
                                            ('5','Pettoriali Distensioni a terra'),
                                            ('6','Pettoriali Distensioni Trx'),('7','Pettoriali Croci manubri'),
                                            ('8','Pettoriali Croci ai cavi Alti'),
                                            ('9','Pettoriali Croci ai cavi bassi'),('10','Pettoriali Parallele'),
                                            ('11','Pettoriali Distensioni manubri panca a 30 gradi')
                                            ])

    spalle = MultiCheckboxField('',
                                   choices=[('12', 'Shoulder Press'), ('13', 'Alzate Laterali '),
                                            ('14', ' Alzate 90 gradi'), ('15', 'Arnold Press'),
                                            ('16', 'Tirate al mento'),
                                            ('17', 'Circonduzioni Delfino'), ('18', 'Flessioni Inverse'),
                                            ('19', 'Alzate laterali cavi bassi')

                                            ])

    dorsali = MultiCheckboxField('',
                                   choices=[('20', 'Lat machine presa pronata'), ('21', 'Lat machine presa supinata '),
                                            ('22', 'Vertical Row Machine'), ('23', 'Vertical row trx'),
                                            ('24', 'Aperture trx'),
                                            ('25', 'Estensioni braccia tese lat machine'), ('26', 'Rowing manubri'),
                                            ('27', 'Aperture 90 gradi')

                                            ])

    bicipiti= MultiCheckboxField('',
                                   choices=[('28', 'Curl manubri'), ('29', 'Curl Bilanciere '),
                                            ('30', 'Curl manubri inclinato'), ('85', 'Curl al cavo basso'),
                                            ('31', 'Curl ai cavi alti'),
                                            ('32', 'Curl trx'), ('33', 'Curl a corpo libero')


                                            ])

    tricipiti= MultiCheckboxField('',
                                   choices=[('34', 'Estensioni cavo alto singolo'), ('35', 'Estensioni cavo alto doppio'),
                                            ('36', 'French Press'), ('37', 'Distensioni su panca'),
                                            ('38', 'French Press trx'),
                                            ('39', 'Parallele')

                                            ])


    addominali= MultiCheckboxField('',
                                   choices=[('40', 'Crunch Base'), ('41', 'Crunch Inverso'),
                                            ('42', 'Crunch Obliqui'), ('43', 'Crunch Completo'),
                                            ('44', 'Criss Cross'),
                                            ('45', 'Rush and Twist'), ('46', 'Torsioni Bilanciere'),
                                            ('47', 'Flessioni laterali con manubrio'),('48','Plank a corpo libero stabilizzato'),
                                            ('49','Plank a corpo libero destabilizzato'),
                                            ('50', 'Side plank isotonico'),('51','Side plank isometrico'),
                                            ('52','Plank con fitball'),('53','Plank con trx')

                                            ])


    dorsali_posturali= MultiCheckboxField('',
                                   choices=[('54', 'Candelabro supino'), ('55', 'Candelabro Prono '),
                                            ('56', 'Superman'), ('57', 'Ponte'),
                                            ('58', 'Libretto'),


                                            ])

    quadricipiti= MultiCheckboxField('',
                                   choices=[('59', 'Pressa monopodalica'), ('60', 'Pressa bipodalica '),
                                            ('61', 'Squat'), ('62', 'Wall Sit'),
                                            ('86', 'Affondi Frontali'),
                                            ('63', 'Affondi laterali'), ('64', 'Squat Jump'),
                                            ('65', 'Salti della corda'),('66','Leg Extension')

                                            ])

    flessori_ginocchio= MultiCheckboxField('',
                                   choices=[('67', 'Leg Curl'), ('68', 'Ponte a corpo libero '),
                                            ('69', 'Ponte sulla fitball monopodalico '),
                                            ('70', ' Ponte sulla fitball bipodalico '),
                                            ('71', ' Dead Lift')

                                            ])

    estensori_anca = MultiCheckboxField('',
                                            choices=[('72', 'Stending Gluteus'), ('73', 'Ponte isotonico '),
                                                     ('74', ' Ponte isometrico'), ('75', ' Stacchi da terra')

                                                     ])
    polpacci = MultiCheckboxField('',
                                            choices=[('76', 'Calf'), ('77', 'Estensioni a ginocchio esteso')

                                                     ])
    adduttori = MultiCheckboxField('',
                                            choices=[('78', 'Adductor machine'), ('79', 'Adduzioni al cavo basso'),
                                                     ('80', 'Adduzioni a corpo libero')
                                                     ])
    abduttori = MultiCheckboxField('',
                                            choices=[('81', 'Abductor machine'), ('82', 'Step Crab'),
                                                     ('83', 'Abduzione al cavo basso'), ('84', 'Abduzione al corpo libero')

                                                     ])

    submit = SubmitField('Crea Allenamento')


class DynamicForm(FlaskForm):



    def append_field(cls, name, field):

        setattr(cls, name, field)
        return cls





