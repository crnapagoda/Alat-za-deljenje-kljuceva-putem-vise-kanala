# Alat za deljenje ključeva putem više kanala

## Osnovna ideja projekta

Ovaj alat omogućava bezbedno deljenje kriptografskih ključeva korišćenjem Shamirs Secret Sharing (SSS) metode. Proces obuhvata generisanje nasumičnog master ključa, njegovu enkripciju, I deljenje tri dela putem email-a, SMS-a I QR koda. Primljeni delovi se mogu rekonstruisati I dekodovati za dobijanje originalnog master ključa.
## Primena u realnom svetu

Kompanija želi da zaštiti trezor. Ako master ključ čuva samo jedna osoba, postoji rizik njegovog gubitka. Primenom SSS metode, ključ se deli na više delova I raspoređuje među ovlašćenim osobama. Za otvaranje trezora potrebni su svi delovi ključa, čime se povećava sigurnost.

#### Još primena:

<ul>
  <li>Deljenje ključa za dekodiranje root ključa za menadžer lozinki. </li>
  <li>Obnavljanje ključa za šifrovane email-ove </li>
  <li>Podela pristupne fraze koja se koristi za rekreaciju glavne tajne, a koja se zatim koristi za pristup kriptovalutnom novčaniku.</li>
</ul>

## Funkcionalnosti

<ul>
  <li>Generisanje I upravljanje ključevima: </li>
    <ul>
      <li>Omogućava korisnicima generisanje nasumičnih kriptografskih ključeva. </li>
      <li>Podržava unos postojećeg ključa za dalju obradu. </li>
    </ul>
  <li>Deljenje ključeva: </li>
    <ul>	
      <li>Implementira Shamirs Secret Sharing metode za deljenje ključa na tri dela. </li>
      <li>Omogućava bezbedno deljenje svakog dela putem različitih kanala: </li>
      <ol>
        <li>Email za prvi deo ključa </li>
        <li>SMS za drugi deo ključa </li>
        <li>QR kod za treći deo ključa </li>
      </ol>
    </ul>
    <li>Rekonstrukcija ključeva: </li> 
    <ul>
      <li>Prikupljanjem svih delova, originalni ključ može biti rekonstruisan. </li>
      <li>Rekonstrukcija je zaštićena pomoću enkripcije, čime se povećava sigurnost. </li>
    </ul>
  <li>Zaštita od neovlašćenog pristupa </li>
    <ul>
      <li>o	Alat se oslanja na kriptografske mehanizme kako bi obezbedio da samo ovlašćeni korisnici mogu rekonstruisati ključ.</li>
    </ul>
</ul>
