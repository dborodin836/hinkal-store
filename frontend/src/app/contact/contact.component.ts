import { Component, OnInit } from '@angular/core';
import { UntypedFormBuilder } from '@angular/forms';
import { ContactService } from '../services/contact.service';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css'],
})
export class ContactComponent implements OnInit {
  contactForm = this.formBuilder.group({
    name: '',
    subject: '',
    email: '',
    message: '',
  });

  constructor(private contactService: ContactService, private formBuilder: UntypedFormBuilder) {}

  onSubmit() {
    console.log('submit');
    console.log(this.contactForm.value);
    this.contactService.sendPost(this.contactForm.value);
  }

  ngOnInit(): void {}
}
