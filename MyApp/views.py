from django.shortcuts import render
from MyApp.forms import FeedbackForm

# Create your views here.
def feedbackview(request):
	f = FeedbackForm()
	if request.method == "POST":
		f=FeedbackForm(request.POST)
		if f.is_valid():
			name = f.cleaned_data['name']
			rollno = f.cleaned_data['rollno']
			email = f.cleaned_data['email']
			feedback = f.cleaned_data['feedback']
			d = {'name':name,'rollno':rollno,'email':email,'feedback':feedback}
			return render(request,'myapp/output.html',d)
	d={'form':f}
	return render(request,'myapp/feedback.html',d)