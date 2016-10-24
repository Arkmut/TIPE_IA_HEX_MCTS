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
enum crduAjouter
{
	DEJA_PRESENT, PLEIN, AJOUTE
};
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
	 Ensemble(int t[],unsigned int nbElements);
    // Mode d'emploi : constructeur a partir d'un tableau c++, avec nbElements la cardinalite max, et la courante, celle effectivement ajout�e
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

//----------------------------------------------------- M�thodes prot�g�es

//----------------------------------------------------- Attributs prot�g�s
unsigned int cardMax;
unsigned int cardAct;
int* tableau;

};

//--------------------------- Autres d�finitions d�pendantes de <${file_base}>

#endif // ${include_guard_symbol}

