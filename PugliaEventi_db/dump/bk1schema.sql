--
-- PostgreSQL database dump
--

-- Dumped from database version 9.1.24
-- Dumped by pg_dump version 10.6 (Ubuntu 10.6-0ubuntu0.18.04.1)

-- Started on 2019-03-13 15:08:20 CET

SET statement_timeout = 0;
--SET lock_timeout = 0;
--SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
--SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 11645)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2009 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 162 (class 1259 OID 16385)
-- Name: utenti; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.utenti (
    id integer NOT NULL,
    username character varying(20) NOT NULL,
    location character varying(40) NOT NULL,
    first_configuration boolean NOT NULL
);


ALTER TABLE public.utenti OWNER TO postgres;

--
-- TOC entry 163 (class 1259 OID 16388)
-- Name: api_utente_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_utente_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.api_utente_id_seq OWNER TO postgres;

--
-- TOC entry 2010 (class 0 OID 0)
-- Dependencies: 163
-- Name: api_utente_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_utente_id_seq OWNED BY public.utenti.id;


--
-- TOC entry 164 (class 1259 OID 16390)
-- Name: valutazioni; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.valutazioni (
    id integer NOT NULL,
    mood character varying(20) NOT NULL,
    companionship character varying(20) NOT NULL,
    rating integer NOT NULL,
    place_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.valutazioni OWNER TO postgres;

--
-- TOC entry 165 (class 1259 OID 16393)
-- Name: api_valutazione_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_valutazione_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.api_valutazione_id_seq OWNER TO postgres;

--
-- TOC entry 2011 (class 0 OID 0)
-- Dependencies: 165
-- Name: api_valutazione_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_valutazione_id_seq OWNED BY public.valutazioni.id;


--
-- TOC entry 166 (class 1259 OID 16395)
-- Name: comuni; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.comuni (
    istat text NOT NULL,
    comune text,
    provincia text,
    regione text,
    prefisso text,
    cap text,
    cod_fis text,
    abitanti numeric,
    link text
);


ALTER TABLE public.comuni OWNER TO postgres;

--
-- TOC entry 167 (class 1259 OID 16401)
-- Name: control; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.control (
    last_update timestamp without time zone,
    id integer NOT NULL
);


ALTER TABLE public.control OWNER TO postgres;

--
-- TOC entry 168 (class 1259 OID 16404)
-- Name: control_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.control_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.control_id_seq OWNER TO postgres;

--
-- TOC entry 2012 (class 0 OID 0)
-- Dependencies: 168
-- Name: control_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.control_id_seq OWNED BY public.control.id;


--
-- TOC entry 169 (class 1259 OID 16406)
-- Name: distanze; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.distanze (
    a text,
    b text,
    distanza numeric,
    autoid integer NOT NULL
);


ALTER TABLE public.distanze OWNER TO postgres;

--
-- TOC entry 170 (class 1259 OID 16412)
-- Name: distanze_autoid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.distanze_autoid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.distanze_autoid_seq OWNER TO postgres;

--
-- TOC entry 2013 (class 0 OID 0)
-- Dependencies: 170
-- Name: distanze_autoid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.distanze_autoid_seq OWNED BY public.distanze.autoid;


--
-- TOC entry 171 (class 1259 OID 16414)
-- Name: eventi; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eventi (
    autoid integer NOT NULL,
    link text,
    titolo text,
    posto_link text,
    posto_nome text,
    data_da timestamp without time zone,
    data_a timestamp without time zone,
    comune text,
    free_entry smallint,
    arte smallint,
    avventura smallint,
    cinema smallint,
    cittadinanza smallint,
    musica_classica smallint,
    geek smallint,
    bambini smallint,
    folklore smallint,
    cultura smallint,
    jazz smallint,
    concerti smallint,
    teatro smallint,
    vita_notturna smallint,
    featured smallint,
    descrizione text,
    popolarita numeric,
    contenuto_html text,
    meteo_bool smallint DEFAULT 0,
    previsioni_bool smallint DEFAULT 0
);


ALTER TABLE public.eventi OWNER TO postgres;

--
-- TOC entry 172 (class 1259 OID 16422)
-- Name: eventi_autoid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.eventi_autoid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eventi_autoid_seq OWNER TO postgres;

--
-- TOC entry 2014 (class 0 OID 0)
-- Dependencies: 172
-- Name: eventi_autoid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.eventi_autoid_seq OWNED BY public.eventi.autoid;


--
-- TOC entry 173 (class 1259 OID 16424)
-- Name: links; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.links (
    id_l integer NOT NULL,
    data_ev text,
    link text,
    titolo text,
    extracted smallint DEFAULT 0
);


ALTER TABLE public.links OWNER TO postgres;

--
-- TOC entry 174 (class 1259 OID 16431)
-- Name: links_id_l_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.links_id_l_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.links_id_l_seq OWNER TO postgres;

--
-- TOC entry 2015 (class 0 OID 0)
-- Dependencies: 174
-- Name: links_id_l_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.links_id_l_seq OWNED BY public.links.id_l;


--
-- TOC entry 175 (class 1259 OID 16433)
-- Name: luoghi; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.luoghi (
    pid integer NOT NULL,
    ext_id numeric,
    nomeposto text,
    tipo text,
    comune text,
    indirizzo text,
    latitudine text,
    longitudine text,
    telefono text,
    sitoweb text,
    chiusura text,
    rating numeric,
    informale smallint,
    raffinato smallint,
    free_entry smallint,
    benessere smallint,
    bere smallint,
    mangiare smallint,
    dormire smallint,
    goloso smallint,
    libri smallint,
    romantico smallint,
    museo smallint,
    spiaggia smallint,
    teatro smallint,
    arte smallint,
    avventura smallint,
    cinema smallint,
    cittadinanza smallint,
    musica_classica smallint,
    geek smallint,
    bambini smallint,
    folklore smallint,
    cultura smallint,
    jazz smallint,
    concerti smallint,
    vita_notturna smallint,
    html text,
    link text
);


ALTER TABLE public.luoghi OWNER TO postgres;

--
-- TOC entry 176 (class 1259 OID 16439)
-- Name: luoghi_dummy; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.luoghi_dummy (
    pid integer NOT NULL,
    nomeposto text,
    informale smallint,
    raffinato smallint,
    free_entry smallint,
    benessere smallint,
    bere smallint,
    mangiare smallint,
    dormire smallint,
    goloso smallint,
    libri smallint,
    romantico smallint,
    museo smallint,
    spiaggia smallint,
    teatro smallint,
    arte smallint,
    avventura smallint,
    cinema smallint,
    cittadinanza smallint,
    musica_classica smallint,
    geek smallint,
    bambini smallint,
    folklore smallint,
    cultura smallint,
    jazz smallint,
    concerti smallint,
    vita_notturna smallint
);


ALTER TABLE public.luoghi_dummy OWNER TO postgres;

--
-- TOC entry 177 (class 1259 OID 16445)
-- Name: luoghi_dummy_pid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.luoghi_dummy_pid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.luoghi_dummy_pid_seq OWNER TO postgres;

--
-- TOC entry 2016 (class 0 OID 0)
-- Dependencies: 177
-- Name: luoghi_dummy_pid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.luoghi_dummy_pid_seq OWNED BY public.luoghi_dummy.pid;


--
-- TOC entry 178 (class 1259 OID 16447)
-- Name: meteo_comuni; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.meteo_comuni (
    autoid integer NOT NULL,
    idcomune text,
    comune text,
    data timestamp without time zone,
    primavera smallint,
    estate smallint,
    autunno smallint,
    inverno smallint,
    sereno smallint,
    coperto smallint,
    poco_nuvoloso smallint,
    pioggia smallint,
    temporale smallint,
    nebbia smallint,
    neve smallint,
    temperatura numeric,
    velocita_vento numeric,
    dati_presenti integer DEFAULT 1
);


ALTER TABLE public.meteo_comuni OWNER TO postgres;

--
-- TOC entry 179 (class 1259 OID 16454)
-- Name: meteo_comuni2_autoid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.meteo_comuni2_autoid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.meteo_comuni2_autoid_seq OWNER TO postgres;

--
-- TOC entry 2017 (class 0 OID 0)
-- Dependencies: 179
-- Name: meteo_comuni2_autoid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.meteo_comuni2_autoid_seq OWNED BY public.meteo_comuni.autoid;


--
-- TOC entry 180 (class 1259 OID 16456)
-- Name: meteo_eventi; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.meteo_eventi (
    autoid integer NOT NULL,
    link text,
    titolo text,
    dataevento timestamp without time zone,
    idevento integer NOT NULL,
    idmeteo integer NOT NULL
);


ALTER TABLE public.meteo_eventi OWNER TO postgres;

--
-- TOC entry 181 (class 1259 OID 16462)
-- Name: meteo_eventi_autoid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.meteo_eventi_autoid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.meteo_eventi_autoid_seq OWNER TO postgres;

--
-- TOC entry 2018 (class 0 OID 0)
-- Dependencies: 181
-- Name: meteo_eventi_autoid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.meteo_eventi_autoid_seq OWNED BY public.meteo_eventi.autoid;


--
-- TOC entry 182 (class 1259 OID 16464)
-- Name: posti_pid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.posti_pid_seq
    START WITH 1
    INCREMENT BY 1
    MINVALUE 0
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.posti_pid_seq OWNER TO postgres;

--
-- TOC entry 2019 (class 0 OID 0)
-- Dependencies: 182
-- Name: posti_pid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.posti_pid_seq OWNED BY public.luoghi.pid;


--
-- TOC entry 183 (class 1259 OID 16466)
-- Name: previsioni_comuni; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.previsioni_comuni (
    autoid integer NOT NULL,
    idcomune text,
    comune text,
    data timestamp without time zone,
    primavera smallint,
    estate smallint,
    autunno smallint,
    inverno smallint,
    sereno smallint,
    coperto smallint,
    poco_nuvoloso smallint,
    pioggia smallint,
    temporale smallint,
    nebbia smallint,
    neve smallint,
    temperatura numeric,
    velocita_vento numeric,
    old smallint
);


ALTER TABLE public.previsioni_comuni OWNER TO postgres;

--
-- TOC entry 184 (class 1259 OID 16472)
-- Name: previsioni_comuni_autoid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.previsioni_comuni_autoid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.previsioni_comuni_autoid_seq OWNER TO postgres;

--
-- TOC entry 2020 (class 0 OID 0)
-- Dependencies: 184
-- Name: previsioni_comuni_autoid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.previsioni_comuni_autoid_seq OWNED BY public.previsioni_comuni.autoid;


--
-- TOC entry 185 (class 1259 OID 16474)
-- Name: previsioni_eventi; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.previsioni_eventi (
    autoid integer NOT NULL,
    link text,
    titolo text,
    dataevento timestamp without time zone,
    idevento integer NOT NULL,
    idprevisione integer NOT NULL
);


ALTER TABLE public.previsioni_eventi OWNER TO postgres;

--
-- TOC entry 186 (class 1259 OID 16480)
-- Name: previsioni_eventi_autoid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.previsioni_eventi_autoid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.previsioni_eventi_autoid_seq OWNER TO postgres;

--
-- TOC entry 2021 (class 0 OID 0)
-- Dependencies: 186
-- Name: previsioni_eventi_autoid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.previsioni_eventi_autoid_seq OWNED BY public.previsioni_eventi.autoid;


--
-- TOC entry 187 (class 1259 OID 16482)
-- Name: sperimentazione; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sperimentazione (
    id integer NOT NULL,
    schema text,
    ordine_lista_a text,
    ordine_lista_b text,
    ordine_lista_c text,
    data_iscr timestamp with time zone,
    data_fine timestamp with time zone,
    test_completato boolean NOT NULL,
    l1 boolean NOT NULL,
    l2 boolean NOT NULL,
    l3 boolean NOT NULL,
    l4 boolean NOT NULL,
    l5 boolean NOT NULL,
    r1 boolean NOT NULL,
    r2 boolean NOT NULL,
    r3 boolean NOT NULL,
    r4 boolean NOT NULL,
    r5 boolean NOT NULL,
    p1 boolean NOT NULL,
    p2 boolean NOT NULL,
    p3 boolean NOT NULL,
    p4 boolean NOT NULL,
    p5 boolean NOT NULL,
    lista_preferita_interesse text,
    user_id integer NOT NULL,
    lista_preferita_personalita text,
    note text
);


ALTER TABLE public.sperimentazione OWNER TO postgres;

--
-- TOC entry 188 (class 1259 OID 16488)
-- Name: sperimentazione_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sperimentazione_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sperimentazione_id_seq OWNER TO postgres;

--
-- TOC entry 2022 (class 0 OID 0)
-- Dependencies: 188
-- Name: sperimentazione_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sperimentazione_id_seq OWNED BY public.sperimentazione.id;


--
-- TOC entry 1840 (class 2604 OID 16490)
-- Name: control id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.control ALTER COLUMN id SET DEFAULT nextval('public.control_id_seq'::regclass);


--
-- TOC entry 1841 (class 2604 OID 16491)
-- Name: distanze autoid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.distanze ALTER COLUMN autoid SET DEFAULT nextval('public.distanze_autoid_seq'::regclass);


--
-- TOC entry 1844 (class 2604 OID 16492)
-- Name: eventi autoid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eventi ALTER COLUMN autoid SET DEFAULT nextval('public.eventi_autoid_seq'::regclass);


--
-- TOC entry 1846 (class 2604 OID 16493)
-- Name: links id_l; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.links ALTER COLUMN id_l SET DEFAULT nextval('public.links_id_l_seq'::regclass);


--
-- TOC entry 1847 (class 2604 OID 16494)
-- Name: luoghi pid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.luoghi ALTER COLUMN pid SET DEFAULT nextval('public.posti_pid_seq'::regclass);


--
-- TOC entry 1848 (class 2604 OID 16495)
-- Name: luoghi_dummy pid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.luoghi_dummy ALTER COLUMN pid SET DEFAULT nextval('public.luoghi_dummy_pid_seq'::regclass);


--
-- TOC entry 1850 (class 2604 OID 16496)
-- Name: meteo_comuni autoid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meteo_comuni ALTER COLUMN autoid SET DEFAULT nextval('public.meteo_comuni2_autoid_seq'::regclass);


--
-- TOC entry 1851 (class 2604 OID 16497)
-- Name: meteo_eventi autoid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meteo_eventi ALTER COLUMN autoid SET DEFAULT nextval('public.meteo_eventi_autoid_seq'::regclass);


--
-- TOC entry 1852 (class 2604 OID 16498)
-- Name: previsioni_comuni autoid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.previsioni_comuni ALTER COLUMN autoid SET DEFAULT nextval('public.previsioni_comuni_autoid_seq'::regclass);


--
-- TOC entry 1853 (class 2604 OID 16499)
-- Name: previsioni_eventi autoid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.previsioni_eventi ALTER COLUMN autoid SET DEFAULT nextval('public.previsioni_eventi_autoid_seq'::regclass);


--
-- TOC entry 1854 (class 2604 OID 16500)
-- Name: sperimentazione id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sperimentazione ALTER COLUMN id SET DEFAULT nextval('public.sperimentazione_id_seq'::regclass);


--
-- TOC entry 1838 (class 2604 OID 16501)
-- Name: utenti id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.utenti ALTER COLUMN id SET DEFAULT nextval('public.api_utente_id_seq'::regclass);


--
-- TOC entry 1839 (class 2604 OID 16502)
-- Name: valutazioni id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.valutazioni ALTER COLUMN id SET DEFAULT nextval('public.api_valutazione_id_seq'::regclass);


--
-- TOC entry 1856 (class 2606 OID 22068)
-- Name: utenti api_utente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.utenti
    ADD CONSTRAINT api_utente_pkey PRIMARY KEY (id);


--
-- TOC entry 1859 (class 2606 OID 22070)
-- Name: utenti api_utente_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.utenti
    ADD CONSTRAINT api_utente_username_key UNIQUE (username);


--
-- TOC entry 1861 (class 2606 OID 22072)
-- Name: valutazioni api_valutazione_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.valutazioni
    ADD CONSTRAINT api_valutazione_pkey PRIMARY KEY (id);


--
-- TOC entry 1866 (class 2606 OID 22074)
-- Name: comuni comuni_istat_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comuni
    ADD CONSTRAINT comuni_istat_key UNIQUE (istat);


--
-- TOC entry 1868 (class 2606 OID 22076)
-- Name: comuni comuni_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comuni
    ADD CONSTRAINT comuni_pkey PRIMARY KEY (istat);


--
-- TOC entry 1870 (class 2606 OID 22078)
-- Name: control control_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.control
    ADD CONSTRAINT control_pkey PRIMARY KEY (id);


--
-- TOC entry 1872 (class 2606 OID 22080)
-- Name: distanze distanze_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.distanze
    ADD CONSTRAINT distanze_pkey PRIMARY KEY (autoid);


--
-- TOC entry 1874 (class 2606 OID 22082)
-- Name: eventi eventi_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eventi
    ADD CONSTRAINT eventi_pkey PRIMARY KEY (autoid);


--
-- TOC entry 1876 (class 2606 OID 22084)
-- Name: links links_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.links
    ADD CONSTRAINT links_pkey PRIMARY KEY (id_l);


--
-- TOC entry 1878 (class 2606 OID 22086)
-- Name: luoghi_dummy luoghi_dummy_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.luoghi_dummy
    ADD CONSTRAINT luoghi_dummy_pkey PRIMARY KEY (pid);


--
-- TOC entry 1881 (class 2606 OID 22088)
-- Name: meteo_comuni meteo_comuni_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meteo_comuni
    ADD CONSTRAINT meteo_comuni_pk PRIMARY KEY (autoid);


--
-- TOC entry 1883 (class 2606 OID 22090)
-- Name: meteo_eventi meteo_eventi_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meteo_eventi
    ADD CONSTRAINT meteo_eventi_pk PRIMARY KEY (autoid);


--
-- TOC entry 1886 (class 2606 OID 22092)
-- Name: previsioni_comuni previsioni_comuni_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.previsioni_comuni
    ADD CONSTRAINT previsioni_comuni_pk PRIMARY KEY (autoid);


--
-- TOC entry 1888 (class 2606 OID 22094)
-- Name: previsioni_eventi previsioni_eventi_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.previsioni_eventi
    ADD CONSTRAINT previsioni_eventi_pk PRIMARY KEY (autoid);


--
-- TOC entry 1890 (class 2606 OID 22096)
-- Name: sperimentazione sperimentazione_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sperimentazione
    ADD CONSTRAINT sperimentazione_pkey PRIMARY KEY (id);


--
-- TOC entry 1857 (class 1259 OID 22097)
-- Name: api_utente_username_3f341d1b_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_utente_username_3f341d1b_like ON public.utenti USING btree (username varchar_pattern_ops);


--
-- TOC entry 1862 (class 1259 OID 22098)
-- Name: api_valutazione_place_id_2a9546f4; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_valutazione_place_id_2a9546f4 ON public.valutazioni USING btree (place_id);


--
-- TOC entry 1863 (class 1259 OID 22099)
-- Name: api_valutazione_user_id_5cc90068; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_valutazione_user_id_5cc90068 ON public.valutazioni USING btree (user_id);


--
-- TOC entry 1864 (class 1259 OID 22100)
-- Name: comuni_comune_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX comuni_comune_idx ON public.comuni USING btree (comune);


--
-- TOC entry 1879 (class 1259 OID 22101)
-- Name: meteo_comuni_autoid_uindex; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX meteo_comuni_autoid_uindex ON public.meteo_comuni USING btree (autoid);


--
-- TOC entry 1884 (class 1259 OID 22102)
-- Name: previsioni_comuni_autoid_uindex; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX previsioni_comuni_autoid_uindex ON public.previsioni_comuni USING btree (autoid);


--
-- TOC entry 1891 (class 1259 OID 22103)
-- Name: sperimentazione_user_id_d19c96ad; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sperimentazione_user_id_d19c96ad ON public.sperimentazione USING btree (user_id);


--
-- TOC entry 1892 (class 2606 OID 22104)
-- Name: valutazioni api_valutazione_user_id_5cc90068_fk_api_utente_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.valutazioni
    ADD CONSTRAINT api_valutazione_user_id_5cc90068_fk_api_utente_id FOREIGN KEY (user_id) REFERENCES public.utenti(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 1893 (class 2606 OID 22109)
-- Name: meteo_comuni meteo_comuni_comuni_istat_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meteo_comuni
    ADD CONSTRAINT meteo_comuni_comuni_istat_fk FOREIGN KEY (idcomune) REFERENCES public.comuni(istat) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 1894 (class 2606 OID 22114)
-- Name: meteo_eventi meteo_eventi_eventi_autoid_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meteo_eventi
    ADD CONSTRAINT meteo_eventi_eventi_autoid_fk FOREIGN KEY (idevento) REFERENCES public.eventi(autoid) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 1895 (class 2606 OID 22119)
-- Name: meteo_eventi meteo_eventi_meteo_comuni_autoid_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meteo_eventi
    ADD CONSTRAINT meteo_eventi_meteo_comuni_autoid_fk FOREIGN KEY (idmeteo) REFERENCES public.meteo_comuni(autoid) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 1896 (class 2606 OID 22124)
-- Name: previsioni_comuni previsioni_comuni_comuni_istat_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.previsioni_comuni
    ADD CONSTRAINT previsioni_comuni_comuni_istat_fk FOREIGN KEY (idcomune) REFERENCES public.comuni(istat) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 1897 (class 2606 OID 22129)
-- Name: previsioni_eventi previsioni_eventi_eventi_autoid_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.previsioni_eventi
    ADD CONSTRAINT previsioni_eventi_eventi_autoid_fk FOREIGN KEY (idevento) REFERENCES public.eventi(autoid) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 1898 (class 2606 OID 22134)
-- Name: previsioni_eventi previsioni_eventi_previsioni_comuni_autoid_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.previsioni_eventi
    ADD CONSTRAINT previsioni_eventi_previsioni_comuni_autoid_fk FOREIGN KEY (idprevisione) REFERENCES public.previsioni_comuni(autoid) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 1899 (class 2606 OID 22139)
-- Name: sperimentazione sperimentazione_user_id_d19c96ad_fk_utenti_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sperimentazione
    ADD CONSTRAINT sperimentazione_user_id_d19c96ad_fk_utenti_id FOREIGN KEY (user_id) REFERENCES public.utenti(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2008 (class 0 OID 0)
-- Dependencies: 6
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2019-03-13 15:08:20 CET

--
-- PostgreSQL database dump complete
--

