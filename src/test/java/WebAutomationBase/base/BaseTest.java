package WebAutomationBase.base;

import static java.lang.System.getenv;

import com.thoughtworks.gauge.AfterScenario;
import com.thoughtworks.gauge.AfterStep;
import com.thoughtworks.gauge.BeforeScenario;
import com.thoughtworks.gauge.BeforeStep;
import com.thoughtworks.gauge.ExecutionContext;
import java.net.URL;
import java.util.HashMap;
import java.util.Locale;
import java.util.Map;

import org.apache.commons.lang3.StringUtils;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.LocalFileDetector;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class BaseTest {


  protected static WebDriver driver;
  protected static WebDriverWait webDriverWait;
  private static Logger logger = LoggerFactory.getLogger(BaseTest.class);

  @BeforeScenario
  public void setUp(ExecutionContext executionContext) throws Exception{

    logger.info("" + executionContext.getCurrentScenario().getName());
    String baseUrl = "https://dpe-preprod.dominos.com.tr/";
    Locale.setDefault(new Locale("en","EN"));

    DesiredCapabilities capabilities = DesiredCapabilities.chrome();

    if (StringUtils.isNotEmpty(getenv("key"))) {
      ChromeOptions options = new ChromeOptions();
      options.addArguments("test-type");
      options.addArguments("disable-popup-blocking");
      options.addArguments("ignore-certificate-errors");
      options.addArguments("disable-translate");
      options.addArguments("--start-maximized");
      options.addArguments("--no-sandbox");
      options.addArguments("incognito");


      String PROXY = "ec2-54-154-66-64.eu-west-1.compute.amazonaws.com:3128";
      Proxy proxy = new org.openqa.selenium.Proxy();
      proxy.setProxyType(Proxy.ProxyType.MANUAL);
      proxy.setHttpProxy(PROXY);
      proxy.setFtpProxy(PROXY);
      proxy.setSslProxy(PROXY);
      capabilities.setCapability(CapabilityType.PROXY, proxy);

      capabilities.setCapability(ChromeOptions.CAPABILITY, options);
      capabilities.setCapability("key", System.getenv("key"));


      driver = new RemoteWebDriver(new URL("http://hub.testinium.io/wd/hub"), capabilities);
      ((RemoteWebDriver) driver).setFileDetector(new LocalFileDetector());
    }
    else if(Platform.getCurrent().toString().contains("WIN")){
      Map<String, Object> prefs = new HashMap<String, Object>();
      prefs.put("profile.default_content_setting_values.notifications", 2);
      ChromeOptions options = new ChromeOptions();
      System.setProperty("webdriver.chrome.driver", "web_driver/chromedriver.exe");
      //      options.addArguments("--kiosk");//FULLSCREEN FOR MAC
      options.addArguments("incognito");
      driver = new ChromeDriver(options);
      driver.manage().window().maximize();
    }
    else {

      Map<String, Object> prefs = new HashMap<String, Object>();
      prefs.put("profile.default_content_setting_values.notifications", 2);

      ChromeOptions options = new ChromeOptions();
      System.setProperty("webdriver.chrome.driver", "web_driver/chromedriver");

      //      options.addArguments("--kiosk");//FULLSCREEN FOR MAC
      options.addArguments("incognito");
      driver = new ChromeDriver(options);
      driver.manage().window().maximize();
    }
    webDriverWait = new WebDriverWait(driver, 45, 150);
    //driver.get(baseUrl);
  }

  @BeforeStep
  public void beforeStep(ExecutionContext executionContext){

    logger.info(executionContext.getCurrentStep().getDynamicText());
  }

  @AfterStep
  public void afterStep(ExecutionContext executionContext){

    if (executionContext.getCurrentStep().getIsFailing()) {
      logger.error(executionContext.getCurrentScenario().getName());
      logger.error(executionContext.getCurrentStep().getDynamicText());
      logger.error(executionContext.getCurrentStep().getErrorMessage() + "\r\n" + executionContext
          .getCurrentStep().getStackTrace());
    }
  }

  @AfterScenario
  public void tearDown(){

    driver.quit();
  }


}
