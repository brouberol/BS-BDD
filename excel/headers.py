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
    u'origine_avant_BS',
    u'filiere_avant_BS',
    u'taille_de_promo_avant_BS',	
    u'classement_avant_BS',
    u'annee_recrutement',
    1, # annee_admission
    u'promo_BS',
    u'scolarite_3e_annee',
    1, # taille_promo_3e annee
    1, # annee_3e_annee
    1, # classement_3e_annee
    u'pays_echange_3e_annee',
    u'universite_echange_3e_annee',
    1, #duree_echange_3e_annee
    u'employeur_stage_3e_annee',
    u'sujet_stage_3e_annee',
    1, # duree_stage_3e_annee
    1, # salaire_stage_3e_annee
    u'scolarite_4e_annee',
    1, # taille_promo_4e annee
    1, # annee_4e_annee,
    1, # classement_4_annee
    u'universite_echange_4e_annee',
    1, #duree_echange_4e_annee
    u'employeur_stage_4e_annee',
    u'sujet_stage_4e_annee',
    1, # duree_stage_4e_annee
    1, # salaire_stage_4e_annee
    u'scolarite_5e_annee',	
    1, # taille_promo_5e_annee	
    1, # annee_5e_annee
    ]  
