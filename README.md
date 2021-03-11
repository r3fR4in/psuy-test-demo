<p>参考该博客 https://www.cnblogs.com/yinjia/p/9503407.html</p>

<p>
	<span>
	目录结构<br>
	config:存放配置文件<br>
	&nbsp&nbsp&nbsp&nbsp setting.py:配置文件<br>
	logs:存放日志文件<br>
	page:存放页面对象类<br>
	&nbsp&nbsp&nbsp&nbsp basePage.py:页面对象基类,其他页面对象类继承该基类<br>
	public:存放公共方法类<br>
	&nbsp&nbsp&nbsp&nbsp baseUnit.py:测试用例基类,其他测试用例类继承该基类<br>
	reportTemplate:存放测试报告模板<br>
	&nbsp&nbsp&nbsp&nbsp HTMLTestRunner.py:旧模板,没有在用<br>
	&nbsp&nbsp&nbsp&nbsp HTMLTestRunnerCN.py:新模板<br>
	service:存放业务实现类,继承页面对象类,根据要测试的业务从页面对象类中调用元素对象组成业务流<br>
	testcase:存放测试用例类,调用业务实现类的方法,使用ddt参数化<br>
	testdata:存放测试数据文件,测试数据用yaml格式保存<br>
	&nbsp&nbsp&nbsp&nbsp uniqueData.yaml:存放需要做唯一校验的数据,每次测试使用后要调用GetYaml.py里的方法+1,避免重复<br>
	run_test:获取testcase下所有文件,批量执行测试用例并输出测试报告<br>
	</span>
</p>
