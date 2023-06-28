import { ComponentFactoryResolver, ComponentRef, Injectable, ViewContainerRef } from '@angular/core';
import { LoaderComponent } from '../loader/loader.component';

@Injectable({
  providedIn: 'root',
})
export class LoaderService {
  rootViewContainer?: ViewContainerRef;
  private component?: ComponentRef<LoaderComponent>;

  constructor(private factoryResolver: ComponentFactoryResolver) {}

  private sleep(ms: number) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }

  public setRootViewContainerRef(viewContainerRef: ViewContainerRef) {
    this.rootViewContainer = viewContainerRef;
  }

  public addLoader() {
    const factory = this.factoryResolver.resolveComponentFactory(LoaderComponent);
    if (this.rootViewContainer) {
      const component = factory.create(this.rootViewContainer.parentInjector);
      this.component = component;
      this.rootViewContainer.insert(component.hostView);
      console.log('Loader added');
    }
  }

  public async removeLoader() {
    if (this.component) {
      // weird
      await this.sleep(200);
      let index = this.rootViewContainer?.indexOf(this.component.hostView);
      this.rootViewContainer?.remove(index);
      console.log('Loader removed');
    }
  }
}
