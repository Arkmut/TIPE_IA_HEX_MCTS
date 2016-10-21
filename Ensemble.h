/*************************************************************************
                           ${file_base}  -  description
                             -------------------
    d�but                : ${date}
    copyright            : (C) ${year} par ${user}
*************************************************************************/

//---------- Interface de la classe Ensemble ------
#if ! defined ( ENSEMBLE_H )
#define ENSEMBLE_H

//--------------------------------------------------- Interfaces utilis�es

//------------------------------------------------------------- Constantes 
int const CARD_MAX=5;
//------------------------------------------------------------------ Types 

//------------------------------------------------------------------------ 
// R�le de la classe Ensemble
//
//
//------------------------------------------------------------------------ 

class Ensemble
{
//----------------------------------------------------------------- PUBLIC

public:
//----------------------------------------------------- M�thodes publiques
    // type M�thode ( liste des param�tres );
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

//------------------------------------------------- Surcharge d'op�rateurs
   
    // Mode d'emploi :
    //
    // Contrat :
    //


//-------------------------------------------- Constructeurs - destructeur
    
    Ensemble(unsigned int cMax=CARD_MAX);
    // Mode d'emploi : constructeur par defaut; cr�e un ensemble vide de taille max cmax
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
//----------------------------------------------------- M�thodes prot�g�es

//----------------------------------------------------- Attributs prot�g�s
unsigned int cardMax;
unsigned int cardAct;
int* tableau;

};

//--------------------------- Autres d�finitions d�pendantes de <${file_base}>

#endif // ${include_guard_symbol}

