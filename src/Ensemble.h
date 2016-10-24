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
enum crduAjouter
{
	DEJA_PRESENT, PLEIN, AJOUTE
};
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
	//n :cardAct
	//m : cardMax
	//{} si l'ensemble est vide
	//{x} singleton
	//{x,y} sinon
	
	//Contrat:

	//TU03
	//TU04
	crduAjouter Ajouter(int aAjouter);
	unsigned int Ajuster(int delta);
	bool Retirer (int element);



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
	 Ensemble(int t[],unsigned int nbElements);
    // Mode d'emploi : constructeur a partir d'un tableau c++, avec nbElements la cardinalite max, et la courante, celle effectivement ajoutée
    //
    // Contrat : taille de t <= nbElements
    //
    virtual ~Ensemble ( );
    // Mode d'emploi :
    //
    // Contrat :
    //

//------------------------------------------------------------------ PRIVE 
private :
	void quicksort(int debut,int fin);
	int partition(int debut,int fin);
	void shift(unsigned int start, int direction);

protected:

//----------------------------------------------------- Méthodes protégées

//----------------------------------------------------- Attributs protégés
unsigned int cardMax;
unsigned int cardAct;
int* tableau;

};

//--------------------------- Autres définitions dépendantes de <${file_base}>

#endif // ${include_guard_symbol}

