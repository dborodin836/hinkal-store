import { TestBed } from '@angular/core/testing';
import { SnackBarMessagesService } from './messages.service';
import { MatSnackBarModule } from '@angular/material/snack-bar';

describe('SnackBarService', () => {
  let service: SnackBarMessagesService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [MatSnackBarModule],
    });
    service = TestBed.inject(SnackBarMessagesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
