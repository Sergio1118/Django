import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import NavbarDashboard from "./components/jsx/navbarDashboard.jsx"; 
import Dashboard from "./components/jsx/dashboard.jsx"; 
import FromSigul from "./components/jsx/fromSigul"; 
import FromLogin from "./components/jsx/fromLogin"; 
import PasswordRecuper from "./components/jsx/passwordRecovery.jsx"; 

function App() {
  
  return (
    <Router>
      {/* Navbar persistente en todas las páginas */}
      <Routes>
        <Route
          path="/registro"
          element={
            <>
              
              <FromSigul />
            </>
          }
        />
        <Route
          path="/login"
          element={
            <>
              <NavbarDashboard />
              <FromLogin />
            </>
          }
        />
        <Route
          path="/recuperar"
          element={
            <>
              <NavbarDashboard />
              <PasswordRecuper />
            </>
          }
        />

        <Route
          path="/dashboard"
          element={
            <>
              <Dashboard />
            </>
          }
        />

        <Route
          path="/"
          element={
            <>
              <Dashboard />
            </>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;
