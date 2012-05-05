def submit_request(request):
    if request.method == 'POST':
        form = SubmitRequest(request.POST)
        if form.is_valid():
            print form
            print dir(form)
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = SubmitRequest() 
        
    return render_to_response('contact.html', {
        'form': form,
    })