import React, { useEffect, useState } from "react";
import api from "../api";
import arrow from "../Images/left-arrow.png";
import printImg from "../Images/download.png";
import InvoiseRow from "../Componants/InvoiseRow";
import AdditionalRow from "../Componants/AdditionalRow";

const Kashf = () => {
    const [clients, setClients] = useState([]);
    const [clientOfKashf, setClientOfKashf] = useState({});
    const [clientInvoises, setClientInvoises] = useState([]);
    const [clientAdditionals, setClientAdditionals] = useState([]);
    const [isPending, setIsPending] = useState(false);
    const [select, setSelect] = useState("");
    const [dropDown, setDropDown] = useState(true);
    const [showClientForm, setShowClientForm] = useState(true);

    useEffect(() => {
        getClients();
    }, []);

    const getClients = async () => {
        const res = await api.get("/api/clients/");
        setClients(res.data);
    };

    const getClientInvoises = async (clientId) => {
        setIsPending(true);
        const res = await api.get(`api/invoises/${clientId}`);
        const data = await res.data;
        setIsPending(false);
        setClientInvoises(data);
    };

    const getClientAdditionals = async (clientId) => {
        setIsPending(true);
        const res = await api.get(`api/additionals/byclientid/${clientId}`);
        const data = await res.data;
        setIsPending(false);
        setClientAdditionals(data);
    };

    const clientClicked = (client) => {
        setSelect(client.name);
        setClientOfKashf(client);
        setDropDown(false);
        setShowClientForm(false);
        getClientInvoises(client.id);
        getClientAdditionals(client.id);
    };

    const print = () => {
        window.print();
    };

    return (
        <div className="kashf-page">
            <h1 className="page-title">كشف حساب</h1>
            {showClientForm && (
                <form onSubmit={() => formSubmit()} className="kashf-form">
                    <i className="fa-regular fa-user"></i>
                    <label className="kashf-form-label">اختر العميل</label>
                    <input
                        value={select}
                        onChange={(e) => {
                            setSelect(e.target.value);
                        }}
                        name="select-value"
                        className="form-input"
                    />
                    {select && dropDown && (
                        <div className="kashf-drop-menu search-drop-menu">
                            {clients
                                .filter((client) => {
                                    const value = select.toLowerCase();
                                    const c = client.name.toLowerCase();

                                    return value && c.startsWith(value) && c;
                                })
                                .map((client) => (
                                    <span
                                        onClick={() => clientClicked(client)}
                                        key={client.id}>
                                        {client.name}
                                    </span>
                                ))}
                        </div>
                    )}
                </form>
            )}
            {!showClientForm && (
                <>
                    <span className="kashf-client-title heighlight-heading">
                        {clientOfKashf.name}
                    </span>
                    <span className="print-btn" onClick={print}>
                        <img src={printImg} alt="" />
                        طباعة
                    </span>
                    <button
                        className="step-back"
                        onClick={() => window.location.reload()}>
                        أختيار عميل اخر <img src={arrow} alt="" />
                    </button>

                    <div className="grid">
                        <div className="child kashf-total-cash">
                            <p className="title">حساب العميل</p>
                            <span className="content">
                                {clientOfKashf.totalCash}
                            </span>
                        </div>
                        <div className="child kashf-received-cash">
                            <p className="title">النقديه المستلمه</p>
                            <span className="content">
                                {clientOfKashf.receivedCash}
                            </span>
                        </div>
                    </div>
                    <div className="kashf-invoises">
                        <table className="table">
                            <thead>
                                <tr>
                                    <td>رقم الفاتوره</td>
                                    <td>اسم الفاتوره</td>
                                    <td>التاريخ</td>
                                    <td>الحساب</td>
                                    <td>الدفع</td>
                                </tr>
                            </thead>
                            <tbody>
                                {clientInvoises.length != 0 ? (
                                    clientInvoises.map((invoise) => (
                                        <tr
                                            key={invoise.id}
                                            className="sorted-row">
                                            <InvoiseRow invoise={invoise} />
                                        </tr>
                                    ))
                                ) : isPending ? (
                                    <span className="loading table-loading"></span>
                                ) : (
                                    <tr key={0} className="notfound">
                                        <td>لا يوجد فواتير مضافة</td>
                                    </tr>
                                )}
                            </tbody>
                        </table>
                    </div>
                    <div className="kashf-additionals">
                        <table className="table">
                            <thead>
                                <tr>
                                    <td>الترتيب</td>
                                    <td>الصنف</td>
                                    <td>العدد</td>
                                    <td>سعر الوحده</td>
                                    <td>الاجمالي</td>
                                </tr>
                            </thead>
                            <tbody>
                                {clientAdditionals.length != 0 ? (
                                    clientAdditionals.map((add) => (
                                        <tr key={add.id} className="sorted-row">
                                            <AdditionalRow additional={add} />
                                        </tr>
                                    ))
                                ) : isPending ? (
                                    <span className="loading table-loading"></span>
                                ) : (
                                    <tr key={0} className="notfound">
                                        <td>لا يوجد أضافات قديمه</td>
                                    </tr>
                                )}
                            </tbody>
                        </table>
                    </div>
                </>
            )}
        </div>
    );
};

export default Kashf;
