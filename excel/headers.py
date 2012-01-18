"""
Definition of Excel row TYPES in function of Django models

These headers are defined to indicate the type of data stored into a column

If the data is of unicode type, the name of the column will be stored (in unicode)

If the data is of another type, a value of this type will be stored, with the name of the 
column indicated with a comment, for clarity

"""

main_header_type = [
    u'nom_insa', 
    u'nom_actuel', 
    u'prenom', 
    1,      # num_etudiant
    u'sexe', 
    u'nationalite',
    u'date_de_naissance', 
    u'adresse_1_(personnelle)', 
    1,      # code_postal_1
    u'adresse_2_(parentale)',  
    1,      # code_postal_2
    u'email_1', 
    u'email_2',
    u'origine_avant_BiM',
    u'filiere_avant_BIM',
    u'taille_de_promo_avant_BIM',	
    u'classement_avant_BIM',
    u'annee_recrutement'
    ]  
