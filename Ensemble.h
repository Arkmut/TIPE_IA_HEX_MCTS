/*************************************************************************
                           ${file_base}  -  description
                             -------------------
    début                : ${date}
    copyright            : (C) ${year} par ${user}
*************************************************************************/

//---------- Interface de la classe Ensemble ------
#if ! defined ( ENSEMBLE_H )
#define ENSEMBLE_H

//--------------------------------------------------- Interfaces utilisées

//------------------------------------------------------------- Constantes 
int const CARD_MAX=5;
//------------------------------------------------------------------ Types 

//------------------------------------------------------------------------ 
// Rôle de la classe Ensemble
//
//
//------------------------------------------------------------------------ 

class Ensemble
{
//----------------------------------------------------------------- PUBLIC

public:
//----------------------------------------------------- Méthodes publiques
    // type Méthode ( liste des paramètres );
    // Mode d'emploi :
    //
    // Contrat :
    //

	//Mode d'emploi:
	//
	//Contrat:

//------------------------------------------------- Surcharge d'opérateurs
   
    // Mode d'emploi :
    //
    // Contrat :
    //


//-------------------------------------------- Constructeurs - destructeur
    
    Ensemble(unsigned int cMax=CARD_MAX);
    // Mode d'emploi :
    //
    // Contrat :
    //

    virtual ~Ensemble ( );
    // Mode d'emploi :
    //
    // Contrat :
    //

//------------------------------------------------------------------ PRIVE 

protected:
//----------------------------------------------------- Méthodes protégées

//----------------------------------------------------- Attributs protégés
unsigned int cardMax;
unsigned int cardAct;
int[]* tableau;

};

//--------------------------- Autres définitions dépendantes de <${file_base}>

#endif // ${include_guard_symbol}

