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
	void Afficher();
	//Mode d'emploi: affichage
	//{} si l'ensemble est vide
	//{x} singleton
	//{x,y} sinon
	//n :cardAct
	//m : cardMax
	//Contrat:

//------------------------------------------------- Surcharge d'opérateurs
   
    // Mode d'emploi :
    //
    // Contrat :
    //


//-------------------------------------------- Constructeurs - destructeur
    
    Ensemble(unsigned int cMax=CARD_MAX);
    // Mode d'emploi : constructeur par defaut; crée un ensemble vide de taille max cmax
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
int* tableau;

};

//--------------------------- Autres définitions dépendantes de <${file_base}>

#endif // ${include_guard_symbol}

