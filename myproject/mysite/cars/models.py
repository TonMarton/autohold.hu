from django.db import models
import os
import datetime
import json
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.dispatch import receiver


def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    return "%s/%s.%s" %("carinstanceimages", "xxxx" ,extension)


class Car(models.Model):

    """
    image_locations - to store the imageinfos like urls in JSON formatted text - set to HiddenInput in admin.py
    """
    image_locations = models.CharField(blank = True, null = True, max_length = 120000)

    """Basics attributes"""
    név = models.CharField(max_length=140, blank = False)
    futott = models.IntegerField(blank = True, null=True)
    évjárat = models.DateField(default=datetime.date.today, blank=True, null=True)
    elsőforgalomba = models.DateField(default=datetime.date.today, blank = True, null=True)
    ár = models.IntegerField(blank = True, null=True)
    motorűrtartam = models.IntegerField(blank = True, null=True)

    henger_elrendezés_choices = (
        ('Soros-Álló','Soros-Álló'),
        ('Soros-Fekvő','Soros-Fekvő'),
        ('V','V'),
        ('Boxer','Boxer'),
        ('W','W'),
        ('Wankel','Wankel')
    )

    henger_elrendezés = models.CharField(max_length=140,null=True,blank = True, choices=henger_elrendezés_choices)
    teljesítmény = models.IntegerField(blank = True, null=True)
    üzemanyagtípus = models.CharField(max_length=140, blank = True, null=True)
    saját_tömeg = models.IntegerField(blank = True, null=True)
    össztömeg = models.IntegerField(blank = True, null=True)
    csomagtartó = models.IntegerField(blank = True, null=True)

    környezetvédelmi_osztály_choices = (
        ('15','15'),
        ('14','14'),
        ('13','13'),
        ('12','12'),
        ('11','11'),
        ('10','10'),
        ('9','9'),
        ('8','8'),
        ('7','7'),
        ('6','6'),
        ('5','5'),
        ('4','4'),
        ('3','3'),
        ('2','2'),
        ('1','1')
    )

    környezetvédelmi_osztály = models.CharField(max_length = 140,blank = True,null = True, choices = környezetvédelmi_osztály_choices)

    seb_váltó_fajta_choices = (
        ('Automata','Automata'),
        ('Félautomata','Félautomata'),
        ('Fokozatmentes-Automata','Fokozatmentes-Automata'),
        ('Szekvenciális','Szekvenciális'),
        ('Tiptronic','Tiptronic')
    )

    seb_váltó_fajta = models.CharField(max_length=140,blank = True,null=True, choices = seb_váltó_fajta_choices)
    seb_váltó_fokozatok = models.IntegerField(blank = True, null=True)

    hajtás_choices = (
        ('Elsőkerék','Elsőkerék'),
        ('Hátsókerék','Hátsókerék'),
        ('Állítható-összkerék','Állítható-összkerék'),
        ('Állandó-összkerék','Állandó-összkerék')
    )

    hajtás = models.CharField(max_length=140,blank = True,null=True, choices = hajtás_choices)
    külső_szín = models.CharField(max_length=140,blank = True, null=True,choices = (('sötét','Sötét'),('világos','Világos')))
    külső_szín_részletes = models.CharField(max_length=140,blank = True, null=True)
    belső_szín = models.CharField(max_length=140,blank = True,null=True,choices = (('sötét','Sötét'),('világos','Világos')))
    belső_szín_részletes = models.CharField(max_length=140,blank = True, null=True)

    klíma_fajta_choices = (
        ('Automata','Automata'),
        ('Digitális','Digitális'),
        ('Digitális-kétzónás','Digitális-kétzónás'),
        ('Digitális-többzónás','Digitális-többzónás')
    )

    klíma_fajta = models.CharField(max_length=140,blank = True, null=True, choices = klíma_fajta_choices)

    tető_fajta_choices = (
        ('Lemeztető','Lemeztető'),
        ('Vászontető','Vászontető'),
        ('Nyitható keménytető','Nyitható keménytető'),
        ('Harmonikatető','Harmonikatető'),
        ('Targatető','Targatető'),
        ('Fix üvegtető','Fix üvegtető'),
        ('Panoráma tető','Panoráma tető'),
        ('Fix napfénytető','Fix napfénytető'),
        ('Nyitható napfénytető','Nyitható napfénytető'),
        ('Elhúzható napfénytető','Elhúzható napfénytető'),
        ('Motoros napfénytető','Motoros napfénytető')
    )

    tető_fajta = models.CharField(max_length=140,blank = True, null=True, choices = tető_fajta_choices)

    kiemeltajánlat = models.BooleanField()

    """Műszaki felszer"""
    stop_go =  models.BooleanField()
    holttérfigyelő =  models.BooleanField()
    sávváltás_figyelmeztető =  models.BooleanField()
    ráfutás_figyelmeztető_aktiv_fék =  models.BooleanField()
    kamera =  models.BooleanField()
    okos_kamera_orr_kamera_360 =  models.BooleanField()
    beparkoló_asszisztens =  models.BooleanField()
    head_up_kivetitő =  models.BooleanField()
    elgurulás_védelem_auto_hold =  models.BooleanField()
    elektromos_kézifék =  models.BooleanField()
    állítható_felfüggesztés = models.BooleanField()
    állítható_kormány = models.BooleanField()
    motoros_kormány_állítás =  models.BooleanField()
    centrálzár = models.BooleanField()
    chiptuning = models.BooleanField()
    defektjavító_készlet = models.BooleanField()
    EDC = models.BooleanField()
    elektromos_ablak_elöl = models.BooleanField()
    elektromos_ablak_hátul = models.BooleanField()
    elektromos_tolótető = models.BooleanField()
    elektromos_tükör = models.BooleanField()
    fedélzeti_komputer = models.BooleanField()
    fűthető_tükör = models.BooleanField()
    kerámia_féktárcsák = models.BooleanField()
    könnyűfém_felni = models.BooleanField()
    kormányváltó =models.BooleanField()
    króm_felni = models.BooleanField()
    kulcsnélküli_indítás = models.BooleanField()
    részecskeszűrő = models.BooleanField()
    riasztó = models.BooleanField()
    sebességfüggő_szervokormány = models.BooleanField()
    sperr_differincálmű = models.BooleanField()
    sportfutómű = models.BooleanField()
    sportülések = models.BooleanField()
    szervokormány = models.BooleanField()
    színezett_üveg = models.BooleanField()
    távolságtartó_tempomat = models.BooleanField()
    tempomat = models.BooleanField()
    tolóajtó = models.BooleanField()
    tolótető = models.BooleanField()
    vonóhorog = models.BooleanField()
    vészfékező =  models.BooleanField()

    """futómű """
    S_LINE =  models.BooleanField()
    adaptiv_légrugó =  models.BooleanField()
    AMG =  models.BooleanField()
    M_SPORT =  models.BooleanField()
    agiliti_kontroll =  models.BooleanField()
    sport_komfort_echo =  models.BooleanField()
    mágneses_lengéscsillapitó =  models.BooleanField()

    alufelni_choices = (
        ('17','17'),
        ('18','18'),
        ('19','19'),
        ('20','20'),
    )

    alufelni =  models.CharField(max_length = 140,blank = True, null=True,choices = alufelni_choices)
    aktiv_kormány =  models.BooleanField()
    dynamic_drive =  models.BooleanField()
    adaptiv_drive =  models.BooleanField()
    összkerék_hajtás =  models.BooleanField()


    """Kényelmi felszer"""
    komfort_bejutás_key_less =  models.BooleanField()
    lábbal_nyitható_csomagtér =  models.BooleanField()
    elektromos_rolók =  models.BooleanField()
    el_tükrök_külső_belső_memória_fényszenzor =  models.BooleanField()
    hővédő_üvegezés =  models.BooleanField()
    akkusztikus_üvegezés =  models.BooleanField()
    b_oszlop_folia =  models.BooleanField()
    négyzónás_klima =  models.BooleanField()
    gerinctámasz =  models.BooleanField()
    kormányfütés =  models.BooleanField()
    sizsák =  models.BooleanField()
    digitális_müszerfal =  models.BooleanField()
    garázsnyitó =  models.BooleanField()
    hazakisérő_fény =  models.BooleanField()
    állófűtés =  models.BooleanField()
    állóhelyzeti_szellőzés =  models.BooleanField()
    bőr_kárpit =  models.BooleanField()
    alcantara_bőr_kárpit =  models.BooleanField()
    start_stop =  models.BooleanField()
    full_extra = models.BooleanField()
    fűthető_ablakmosó_fúvókák = models.BooleanField()
    fűthető_szélvédő = models.BooleanField()
    fűthető_ülés = models.BooleanField()
    álló_helyzeti_klíma = models.BooleanField()
    hűthető_kartámasz = models.BooleanField()
    hűthető_kesztyűtartó = models.BooleanField()
    üléshűtés_szellőztetés = models.BooleanField()
    bőr_belső = models.BooleanField()
    műbőr_kárpit = models.BooleanField()
    velúr_kárpit = models.BooleanField()
    soft_close_ajtó_szervó =  models.BooleanField()
    állítható_combtámasz = models.BooleanField()
    állítható_hátsó_ülések = models.BooleanField()
    automata_csomagtérajtó = models.BooleanField()
    automata_sötétedő_belsőtükör = models.BooleanField()
    automata_sötétedő_külsőtükör = models.BooleanField()
    bőrszövet_huzat = models.BooleanField()
    deréktámasz = models.BooleanField()
    dönthető_utasülések = models.BooleanField()
    elektromos_ülésállítás_utasoldal = models.BooleanField()
    elektromos_ülésállítás_vezetőoldal = models.BooleanField()
    elektromos_fejtámlák = models.BooleanField()
    elektromos_behajtható_tükrök = models.BooleanField()
    elektronikus_futómű_hangolás = models.BooleanField()
    faberakás = models.BooleanField()
    középső_kartámasz = models.BooleanField()
    masszírozós_ülés = models.BooleanField()
    memóriás_vezetőülés = models.BooleanField()
    motoros_memóriás_ülések =  models.BooleanField()
    multifunkciós_kormánykerék = models.BooleanField()
    plüss_kárpit = models.BooleanField()
    pótkerék = models.BooleanField()
    távolsági_fényszóró_asszisztens = models.BooleanField()
    tolatókamera = models.BooleanField()
    tolatóradar = models.BooleanField()
    ülésmagasság_állítás = models.BooleanField()

    """Biztonsági felszer"""
    függönylégzsák = models.BooleanField()
    gyalogos_légzsák = models.BooleanField()
    hátsó_oldal_légzsák = models.BooleanField()
    kikapcsolható_légzsák = models.BooleanField()
    oldallégzsák =models.BooleanField()
    térdlégzsák =models.BooleanField()
    utasoldali_légzsák =models.BooleanField()
    vezetőoldali_légzsák =models.BooleanField()
    bixenon_fényszóró =models.BooleanField()
    bukólámpa =models.BooleanField()
    éjjellátó_asszisztens =models.BooleanField()
    fényszóró_magasságállítás =models.BooleanField()
    fényszóró_mosó =models.BooleanField()
    kanyarkövető_fényszóró =models.BooleanField()
    kiegészítő_fényszóró =models.BooleanField()
    ködlámpa =models.BooleanField()
    LED_fényszóró =models.BooleanField()
    mátrix_LED =  models.BooleanField()
    adaptiv_LED =  models.BooleanField()
    xenon_fényszóró = models.BooleanField()
    lézer_fény =  models.BooleanField()
    multibeam =  models.BooleanField()
    led_hátsó_lámpák =  models.BooleanField()
    ABS_blokkolásgátló = models.BooleanField()
    ADS_adaptívlengéscsillapító = models.BooleanField()
    APS_parkolóradar =models.BooleanField()
    ARD_autómatikustávolságtartó =models.BooleanField()
    ASR_kipörgésgátló =models.BooleanField()
    beépített_gyerekülés =models.BooleanField()
    bukócső =models.BooleanField()
    csomag_rögzítő =models.BooleanField()
    defekktűrő_abroncsok =models.BooleanField()
    EBD_EBV_elektronikusfékerő_elosztó =models.BooleanField()
    EDS_elektronikus_diferenciálzár =models.BooleanField()
    esőszenzor =models.BooleanField()
    ESP_menetstabilizátor =models.BooleanField()
    fékasszisztens =models.BooleanField()
    GPS_nyomkövető =models.BooleanField()
    guminyomásellenőrző_rendszer =models.BooleanField()
    hátsó_fejtámlák =models.BooleanField()
    indításgátló_immobiliser =models.BooleanField()
    ISOFIX_rendszer =models.BooleanField()
    lejtmenet_asszisztens =models.BooleanField()
    MSR_motorféknyomás_szabályzás =models.BooleanField()
    rablásgátló =models.BooleanField()
    sávtartó_rendszer =models.BooleanField()
    sebességváltó_zár =models.BooleanField()
    táblafelismerő_funkció =models.BooleanField()
    visszagurulás_gátló =models.BooleanField()

    """Hifi és multimédia"""
    autótelefon =models.BooleanField()
    CDs_autórádió =models.BooleanField()
    DVD =models.BooleanField()
    GPS =models.BooleanField()
    HIFI =models.BooleanField()
    rádió =models.BooleanField()
    rádiós_magnó =models.BooleanField()
    TV =models.BooleanField()
    DIN_1db =models.BooleanField()
    DIN_2db =models.BooleanField()
    CD_tár =models.BooleanField()
    MP3_lejátszás =models.BooleanField()
    MP4_lejátszás =models.BooleanField()
    WMA_lejátszás =models.BooleanField()
    analóg_TV_tuner =models.BooleanField()
    AUX_csatlakozó =models.BooleanField()
    bluetooth_kihangosító =models.BooleanField()
    DVB_tuner =models.BooleanField()
    DVBT_tuner =models.BooleanField()
    erősító_kimenet =models.BooleanField()
    FM_transzmitter =models.BooleanField()
    HDMI_bemenet =models.BooleanField()
    iPhone_iPod_csatlakozó =models.BooleanField()
    kihangosító =models.BooleanField()
    memóriakártya_olvasó =models.BooleanField()
    merevlemez =models.BooleanField()
    mikrofon_bemenet =models.BooleanField()
    tolatókamera_bemenet =models.BooleanField()
    USB_csatlakozó =models.BooleanField()
    érintőkijelző =models.BooleanField()
    erősítő =models.BooleanField()
    fejtámlamonitor =models.BooleanField()
    gyári_erősítő =models.BooleanField()
    kormányra_szerelhető_távirányító =models.BooleanField()
    távirányító =models.BooleanField()
    tetőmonitor =models.BooleanField()
    touchpad =  models.BooleanField()
    beszédvezérlés =  models.BooleanField()
    smartphone =  models.BooleanField()
    apple_carplay =  models.BooleanField()
    burmester = models.BooleanField()
    harman_kardon = models.BooleanField()
    bose = models.BooleanField()
    bang_and_olufsen = models.BooleanField()
    sim =  models.BooleanField()
    sd =  models.BooleanField()
    dvd_cd =  models.BooleanField()
    mmi_pluss =  models.BooleanField()
    professional =  models.BooleanField()
    widescreen =  models.BooleanField()
    internet =  models.BooleanField()
    app_letöltés =  models.BooleanField()
    vezeték_nélküli_töltés =  models.BooleanField()
    digitális_rádió =  models.BooleanField()

    hangszóró_számok_choices = (
        ('2','2'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12')
    )

    hangszórók_száma = models.CharField(max_length = 140,blank = True, null=True,choices = hangszóró_számok_choices)
    mélynyomó = models.BooleanField()

    """Egyéb information"""
    garanciális =models.BooleanField()
    azonnal_elvihető =models.BooleanField()
    bemutató_jármű =models.BooleanField()
    jobbkormányos =models.BooleanField()
    rendelhető =models.BooleanField()
    autóbeszámítás_lehetséges =models.BooleanField()
    első_tulajtól =models.BooleanField()
    frissen_szervizelt =models.BooleanField()
    garázsban_tartott =models.BooleanField()
    keveset_futott =models.BooleanField()
    második_tulajdonostól =models.BooleanField()
    motorbeszámítás_lehetséges =models.BooleanField()
    mozgássérült =models.BooleanField()
    nem_dohányzó =models.BooleanField()
    rendszeresen_karbantartott =models.BooleanField()
    szervizkönyv =models.BooleanField()
    törzskönyv =models.BooleanField()

    leírás = models.CharField(max_length=1000, blank = True, null=True)

    pipálható_extra_név1 = models.CharField(max_length=100, blank = True)
    pipálható_extra_név2 =models.CharField(max_length=100, blank = True)
    pipálható_extra_név3 =models.CharField(max_length=100, blank = True)
    pipálható_extra_név4 =models.CharField(max_length=100, blank = True)
    pipálható_extra_név5 =models.CharField(max_length=100, blank = True)

    kitölthető_extra_név1 =models.CharField(max_length=100, blank = True)
    kitölthető_extra_érték1 =models.CharField(max_length=100, blank = True)

    kitölthető_extra_név2 =models.CharField(max_length=100, blank = True)
    kitölthető_extra_érték2 =models.CharField(max_length=100, blank = True)

    kitölthető_extra_név3 =models.CharField(max_length=100, blank = True)
    kitölthető_extra_érték3 =models.CharField(max_length=100, blank = True)

    kitölthető_extra_név4 =models.CharField(max_length=100, blank = True)
    kitölthető_extra_érték4 =models.CharField(max_length=100, blank = True)

    kitölthető_extra_név5 =models.CharField(max_length=100, blank = True)
    kitölthető_extra_érték5 =models.CharField(max_length=100, blank = True)

    def __str__(self):
        string = self.név + " (" + self.elsőforgalomba.strftime('%Y/%m/%d') + ")"
        return string

@receiver(models.signals.post_delete, sender=Car)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes files from filesystem
    when corresponding `Car` object is deleted.
    """
    image_locations = instance.image_locations
    if image_locations is None:
        return True
    if image_locations == '':
        return True
    else:
        dataObject = json.loads(instance.image_locations)
        fs = FileSystemStorage(settings.MEDIA_ROOT + "/carinstanceimages/")

        for image in dataObject:
            fs.delete(image['name'])



# @receiver(models.signals.pre_save, sender=Car)
# def auto_delete_file_on_change(sender, instance, **kwargs):
#     """
#     Deletes old file from filesystem
#     when corresponding `MediaFile` object is updated
#     with new file.
#     """
#     if not instance.pk:
#         return False
#
#     if instance.kép1:
#         try:
#             old_file = Car.objects.get(pk=instance.pk).kép1
#         except Car.DoesNotExist:
#             return False
#
#     new_file = instance.kép1
#     if not old_file == new_file:
#         if os.path.isfile(old_file.path):
#             os.remove(old_file.path)

class Kiemelt_szoveg(models.Model):
    szöveg = models.CharField(max_length=100, blank = True)

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)
