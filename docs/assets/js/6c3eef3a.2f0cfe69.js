"use strict";(self.webpackChunkcptdocs=self.webpackChunkcptdocs||[]).push([[300],{8676:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>p,contentTitle:()=>s,default:()=>u,frontMatter:()=>o,metadata:()=>a,toc:()=>c});var i=t(7624),r=t(2172);const o={sidebar_position:0,description:"Retrieve the input in Agent"},s="Input data",a={id:"agent/input",title:"Input data",description:"Retrieve the input in Agent",source:"@site/docs/agent/input.md",sourceDirName:"agent",slug:"/agent/input",permalink:"/Captain/docs/agent/input",draft:!1,unlisted:!1,tags:[],version:"current",sidebarPosition:0,frontMatter:{sidebar_position:0,description:"Retrieve the input in Agent"},sidebar:"docSidebar",previous:{title:"Agent",permalink:"/Captain/docs/category/agent"},next:{title:"Metadata",permalink:"/Captain/docs/agent/metadata"}},p={},c=[];function d(e){const n={a:"a",admonition:"admonition",br:"br",code:"code",em:"em",h1:"h1",p:"p",pre:"pre",...(0,r.M)(),...e.components};return(0,i.jsxs)(i.Fragment,{children:[(0,i.jsx)(n.h1,{id:"input-data",children:"Input data"}),"\n",(0,i.jsx)(n.p,{children:"At this step you have your first agent. For the sake of simplicity, we have chosen not to provide the input to the agent (or maybe he doesn't need it)."}),"\n",(0,i.jsxs)(n.p,{children:["We will now provide the input param (",(0,i.jsx)(n.em,{children:"file"})," by default) to the agent."]}),"\n",(0,i.jsx)(n.admonition,{type:"important",children:(0,i.jsxs)(n.p,{children:["The page ",(0,i.jsx)(n.a,{href:"/docs/captain/input",children:"Modify Captain's input"})," outlines the steps to change the input.",(0,i.jsx)(n.br,{}),"\n","For example, if you want to use ",(0,i.jsx)(n.code,{children:"-u <username>"})," or ",(0,i.jsx)(n.code,{children:"-w <website>"}),", or even remove the need of any input for your project."]})}),"\n",(0,i.jsx)("br",{}),"\n",(0,i.jsxs)(n.p,{children:["For this example, i'm taking back our previously created ",(0,i.jsx)(n.em,{children:"Agent"})," ",(0,i.jsx)(n.code,{children:"my-parser"}),"."]}),"\n",(0,i.jsx)(n.pre,{children:(0,i.jsx)(n.code,{className:"language-python",metastring:'title="agents/my-parser.py"',children:'from ..base import Base, logger\n\nclass MyParserAgent(Base):\n    NAME = "MyParser"\n    ACTIVATED = True\n    VERSION = "1.0"\n    MISSION = "Yet another parser to parse"\n    FILE = None  # New property\n\n    def __init__(self, file):  # New function\n        self.FILE = file  # New property\n\n    def mission(self):\n        logger.info(f\'[{self.NAME}] Checking in.\')\n\n        if self.file:  # Agent can now access the argument (file)\n            with open(file, "rb") as f:  # And process it ...\n                ...\n            logger.info(f\'[{self.NAME}] Parsing file\')\n        return <your-output>\n'})})]})}function u(e={}){const{wrapper:n}={...(0,r.M)(),...e.components};return n?(0,i.jsx)(n,{...e,children:(0,i.jsx)(d,{...e})}):d(e)}},2172:(e,n,t)=>{t.d(n,{I:()=>a,M:()=>s});var i=t(1504);const r={},o=i.createContext(r);function s(e){const n=i.useContext(o);return i.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function a(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(r):e.components||r:s(e.components),i.createElement(o.Provider,{value:n},e.children)}}}]);