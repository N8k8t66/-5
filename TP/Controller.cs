using CalculatorApp.Models;
using Microsoft.AspNetCore.Mvc;
using System.Net.Security;
using System.Runtime.InteropServices;

namespace WebApplication1665.Controllers
{
    public class HomeController : Controller
    {
        public ViewResult Index()
        {
            int hour = DateTime.Now.Hour;
            ViewBag.Greeting = hour < 12 ? "Доброе утро" : "Доброго дня";
            return View();
        }
        [HttpGet]
        public ViewResult RsvpForm()
        {
            return View();
        }
        [HttpPost]
        public ViewResult RsvpForm(CalculatorModel model, string submitButton)
        {

            if (submitButton == "Очистить")
            {
                model.Operand1 = 0;
                model.Operand2 = 0;
                model.Operation = null;
                model.result = 0;
                ModelState.Clear();

                return View(model);
            }
            if (submitButton == "Вычислить")
            {
                if (ModelState.IsValid)
                {
                    switch (model.Operation)
                    {
                        case "+":
                            model.result = model.Operand1 + model.Operand2;
                            break;
                        case "-":
                            model.result = model.Operand1 + model.Operand2;
                            break;
                        case "*":
                            model.result = model.Operand1 * model.Operand2;
                            break;
                    }
                ViewBag.ExpectedValue = 23;
                }
            }
            return View(model);
        }
    }
}
