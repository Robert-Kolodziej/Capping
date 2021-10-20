function getData()
{
   var InstitutionName= document.getElementById("institution_name").value;
   var DegreeName= document.getElementById("degree_name").value;
   var Dates = document.getElementById("dates").value;
   var Description= document.getElementById("description").value;

   //localStorage.setItem("txtValue", Institution name);
   //localStorage.setItem("txtValue1", Degree name);
   //localStorage.setItem("txtValue2", Dates);
   //localStorage.setItem("txtValue3", Description);
   var institutionInput = <HTMLInputElement> document.getElementById("institution");
   institutionInput.value = institutionInput.value+ InstitutionName;


}