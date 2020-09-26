function check()
{
	alert('hi');
	var phn = document.f.phn.value;
	if(phn.length<10)
	{
		alert('write numbers');
		return true;
	}
	else
	{
		alert('correct');
		return false;
	}
	return false;
}