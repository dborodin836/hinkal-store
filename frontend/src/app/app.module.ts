import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';
import { Routes, RouterModule } from '@angular/router';
import { MatPaginatorModule } from '@angular/material/paginator';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { AboutComponent } from './about/about.component';
import { StoreComponent } from './store/store.component';
import { DishDetailComponent } from './dish-detail/dish-detail.component';
import { FooterComponent } from './footer/footer.component';
import { HeaderComponent } from './header/header.component';
import { NavbarComponent } from './navbar/navbar.component';
import { ContactComponent } from './contact/contact.component';
import { LoginComponent } from './login/login.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { SuccessComponent } from './success/success.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { CheckoutComponent } from './checkout/checkout.component';
import { RegisterComponent } from './register/register.component';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { AccountActivationComponent } from './account-activation/account-activation.component';
import { ForbiddenComponent } from './forbidden/forbidden.component';
import { VendorLoginComponent } from './vendor-login/vendor-login.component';
import { VendorRegisterComponent } from './vendor-register/vendor-register.component';

const appRoutes: Routes = [
  { path: '', component: HomeComponent, title: 'Marketplace Hinkal' },
  { path: 'about', component: AboutComponent, title: 'MH | About Us' },
  { path: 'store', component: StoreComponent, title: 'MH | Store' },
  { path: 'store/:id', component: DishDetailComponent, title: 'MH | Detailed' },
  { path: 'contact', component: ContactComponent, title: 'MH | Contact Us' },
  { path: 'login', component: LoginComponent, title: 'MH | Login' },
  { path: 'login-vendor', component: VendorLoginComponent, title: 'MH | Login as Vendor' },
  { path: 'register', component: RegisterComponent, title: 'MH | Register' },
  { path: 'register-vendor', component: RegisterComponent, title: 'MH | Register as Vendor' },
  { path: 'dashboard', component: DashboardComponent, title: 'MH | Dashboard' },
  { path: 'success', component: SuccessComponent, title: 'MH | Success!' },
  { path: 'cart', component: CheckoutComponent, title: 'MH | Cart' },
  { path: 'account-activation', component: AccountActivationComponent, title: 'Marketplace Hinkal' },
  { path: '**', component: NotFoundComponent, title: 'MH | Not Found' },
];

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NotFoundComponent,
    AboutComponent,
    StoreComponent,
    DishDetailComponent,
    FooterComponent,
    HeaderComponent,
    NavbarComponent,
    ContactComponent,
    LoginComponent,
    DashboardComponent,
    SuccessComponent,
    CheckoutComponent,
    RegisterComponent,
    AccountActivationComponent,
    ForbiddenComponent,
    VendorLoginComponent,
    VendorRegisterComponent,
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(appRoutes),
    HttpClientModule,
    ReactiveFormsModule,
    HttpClientXsrfModule,
    BrowserAnimationsModule,
    MatPaginatorModule,
    FormsModule,
    MatSnackBarModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
