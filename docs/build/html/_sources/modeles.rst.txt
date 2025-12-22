Modèles de données
==================

La base de données repose sur trois modèles

Modèle Profile
--------------
- ``user``              : ``OneToOneField(User)``
- ``favorite_city``     : ``CharField(max_length=64, blank=True)``

Modèle Address
--------------
- ``number``            : ``PositiveIntegerField()``  
- ``street``            : ``CharField(max_length=64)``  
- ``city``              : ``CharField(max_length=64)``  
- ``state``             : ``CharField(max_length=2)``  
- ``zip_code``          : ``CharField(max_length=5)``  
- ``country_iso_code``  : ``CharField(max_length=3)``  

Modèle Letting
--------------
- ``title``             : ``CharField(max_length=256)``  
- ``address``           : ``OneToOneField(Address, on_delete=models.CASCADE)``
