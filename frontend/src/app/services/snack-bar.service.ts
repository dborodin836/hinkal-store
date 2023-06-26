import {Injectable} from '@angular/core';
import {MatSnackBar} from "@angular/material/snack-bar";

@Injectable({
  providedIn: 'root'
})
export class SnackBarService {

  constructor(private snackBar: MatSnackBar) {
  }

  openSnackBar(message: string, action?: string, durationMs?: number, level?: "warning" | "error" | "success"): void {
    let panelClass: Array<string> = [];
    if (!action) action = "X";
    if (!durationMs) durationMs = 7 * 1000;

    switch (level) {
      case "warning":
        panelClass.push("warning-snackbar");
        break;
      case "error":
        panelClass.push("error-snackbar");
        break;
      case "success":
        panelClass.push("success-snackbar");
        break;
    }

    this.snackBar.open(message, action, {
      duration: durationMs,
      horizontalPosition: 'end',
      panelClass: panelClass
    });
  }
}
